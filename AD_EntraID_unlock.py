# ad_unlock_report.py
# Requires ldap3; install with: pip install ldap3
#
# PURPOSE:
#   1. Scan Active Directory for locked-out user accounts.
#   2. Prompt for approval before unlocking each one (no blind mass-unlock).
#   3. Generate a CSV report of every action taken.
#   4. Send an email notification summarizing what happened.
#
# SECURITY NOTES (read before using in a real environment):
#   - This script requires an AD service account with UNLOCK rights only —
#     not Domain Admin. Least privilege matters; over-permissioned service
#     accounts are a common real-world attack target.
#   - Credentials below are placeholders. NEVER hardcode real passwords in
#     a script. Use environment variables or a secrets manager instead
#     (e.g. os.environ.get("AD_SERVICE_PASSWORD")).
#   - The manual confirm step (Step 3) is intentional — auto-unlocking
#     every locked account defeats the purpose of lockout policies, which
#     exist to slow down brute-force attempts.
#   - Every unlock action is logged to the CSV so there's a clear audit
#     trail of who got unlocked, when, and by what tool.

from ldap3 import Server, Connection, ALL, MODIFY_REPLACE
import csv
from datetime import datetime
import smtplib
from email.message import EmailMessage

# ---------------------------------------------------------------------------
# STEP 0: CONFIG — fill these in once your homelab AD access is set up
# ---------------------------------------------------------------------------
AD_SERVER = "ldap://DC01.SOCLAB.local"       # your domain controller
AD_USER = "SOCLAB\\svc_unlock"               # service account, unlock rights only
AD_PASSWORD = "REPLACE_ME"                    # move to env var before real use
SEARCH_BASE = "DC=SOCLAB,DC=local"           # base DN to search under

NOTIFY_EMAIL_FROM = "soc-automation@soclab.local"
NOTIFY_EMAIL_TO = "soc-team@soclab.local"
SMTP_SERVER = "smtp.soclab.local"

REPORT_FILE = "ad_unlock_report.csv"

# ---------------------------------------------------------------------------
# STEP 1: Connect to AD
# ---------------------------------------------------------------------------
def connect_to_ad():
    server = Server(AD_SERVER, get_info=ALL)
    conn = Connection(server, user=AD_USER, password=AD_PASSWORD, auto_bind=True)
    return conn

# ---------------------------------------------------------------------------
# STEP 2: Search for locked accounts
#   lockoutTime is nonzero when an account is currently locked out.
# ---------------------------------------------------------------------------
def find_locked_accounts(conn):
    conn.search(
        search_base=SEARCH_BASE,
        search_filter="(&(objectClass=user)(lockoutTime>=1))",
        attributes=["sAMAccountName", "lockoutTime", "distinguishedName"]
    )
    return conn.entries  # list of matching AD account objects

# ---------------------------------------------------------------------------
# STEP 3: Unlock — with a manual confirm gate per account
#   This is the guardrail against blind mass-unlocking.
# ---------------------------------------------------------------------------
def unlock_account(conn, entry, report_rows):
    username = str(entry.sAMAccountName)
    dn = str(entry.distinguishedName)

    # Require explicit human confirmation before unlocking each account
    answer = input(f"Unlock account '{username}'? (y/n): ").strip().lower()
    if answer != "y":
        print(f"Skipped {username}.")
        return

    # lockoutTime = 0 is how AD represents "not locked"
    conn.modify(dn, {"lockoutTime": [(MODIFY_REPLACE, [0])]})

    if conn.result["result"] == 0:
        print(f"Unlocked: {username}")
        report_rows.append({
            "username": username,
            "action": "unlocked",
            "timestamp": datetime.now().isoformat(),
            "performed_by": AD_USER
        })
    else:
        print(f"Failed to unlock {username}: {conn.result}")

# ---------------------------------------------------------------------------
# STEP 4: Write CSV report — the audit trail
# ---------------------------------------------------------------------------
def write_report(report_rows):
    with open(REPORT_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["username", "action", "timestamp", "performed_by"])
        writer.writeheader()
        writer.writerows(report_rows)
    print(f"Report written to {REPORT_FILE}")

# ---------------------------------------------------------------------------
# STEP 5: Email notification to the SOC team
# ---------------------------------------------------------------------------
def send_notification(report_rows):
    if not report_rows:
        print("No accounts were unlocked — skipping notification.")
        return

    msg = EmailMessage()
    msg["Subject"] = f"AD Account Unlock Report — {datetime.now().strftime('%Y-%m-%d')}"
    msg["From"] = NOTIFY_EMAIL_FROM
    msg["To"] = NOTIFY_EMAIL_TO

    body_lines = [f"{r['username']} unlocked at {r['timestamp']} by {r['performed_by']}" for r in report_rows]
    msg.set_content("Accounts unlocked today:\n\n" + "\n".join(body_lines))

    with smtplib.SMTP(SMTP_SERVER) as server:
        server.send_message(msg)
    print("Notification email sent.")

# ---------------------------------------------------------------------------
# MAIN — ties all the steps together
# ---------------------------------------------------------------------------
def main():
    conn = connect_to_ad()
    locked = find_locked_accounts(conn)

    if not locked:
        print("No locked accounts found.")
        return

    print(f"Found {len(locked)} locked account(s).")
    report_rows = []
    for entry in locked:
        unlock_account(conn, entry, report_rows)

    write_report(report_rows)
    send_notification(report_rows)

if __name__ == "__main__":
    main()
