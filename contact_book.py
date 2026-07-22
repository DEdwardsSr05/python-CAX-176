# David Edwards
# 2026-CAX-176
# July 21, 2026
# SBA 351
# Contact Book

"""
Design notes (per submission write-up requirement):
- Contacts are stored in a single dictionary: { name (str) : phone (str) }
  A dict was chosen over a list because it enforces unique keys (names)
  automatically and gives O(1) lookup for search/delete instead of
  looping through a list every time.
- Each menu action lives in its own function and takes `contacts` as a
  parameter, then modifies it in place (dicts are mutable, so no return
  value is needed to "save" changes back).
- The main() loop just handles menu display + routing; it does not
  contain any contact logic itself. That separation is what the rubric
  calls "code reusability and modularity."
- Challenge: validating the menu choice. Input from input() is always a
  string, so converting to int() can throw a ValueError if the user
  types something like "abc". That's handled with try/except rather
  than checking .isdigit(), so non-numeric input is caught cleanly.
"""


def add_contact(contacts):
    """Prompt for a name and phone number, add to the dict if the name
    doesn't already exist. Duplicate names are rejected (not overwritten)."""
    name = input("Enter contact name: ").strip()

    # Basic input validation - don't allow a blank name
    if name == "":
        print("Name cannot be empty. Contact not added.")
        return

    # Dictionary keys are unique by nature, but we still need to check
    # ourselves and print a message - otherwise add_contact would just
    # silently overwrite the existing number.
    if name in contacts:
        print(f"A contact named '{name}' already exists. Not added.")
        return

    phone = input("Enter phone number: ").strip()

    # Simple validation: digits only, and a reasonable length (7-15
    # covers most real-world phone number lengths without being strict
    # about area codes/country codes/dashes).
    if not phone.isdigit() or not (7 <= len(phone) <= 15):
        print("Invalid phone number. Use digits only (7-15 digits). Contact not added.")
        return

    contacts[name] = phone
    print(f"Contact '{name}' added.")


def view_contacts(contacts):
    """Display all contacts. Prints a message instead of an empty list
    if there are none yet."""
    if not contacts:  # empty dict is "falsy" in Python
        print("Contact list is empty.")
        return

    print("\n--- Contact List ---")
    # sorted() on a dict iterates its keys alphabetically - easy way to
    # satisfy the "optional: sort by name" enhancement for free.
    for name in sorted(contacts):
        print(f"{name}: {contacts[name]}")
    print("---------------------\n")


def search_contact(contacts):
    """Ask for a name (or partial name) and print any matches.
    Case-insensitive substring match, so 'dav' matches 'David'."""
    query = input("Enter name (or part of name) to search: ").strip().lower()

    matches = {name: phone for name, phone in contacts.items()
               if query in name.lower()}

    if not matches:
        print(f"No contacts matching '{query}' were found.")
        return

    print("--- Matches ---")
    for name in sorted(matches):
        print(f"{name}: {matches[name]}")
    print("---------------")


def delete_contact(contacts):
    """Ask for a name and remove it if present."""
    name = input("Enter the name of the contact to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"No contact named '{name}' was found.")


def main():
    """Main menu loop. Handles display + routing only - no contact
    logic lives here, it's delegated to the functions above."""
    contacts = {}  # single source of truth for all contact data

    menu_text = """
Contact Book Menu:
1. Add New Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Exit
"""

    while True:
        print(menu_text)
        choice_input = input("Enter your choice (1-5): ").strip()

        # try/except handles the case where the user types something
        # that isn't a number at all (e.g. "five") instead of crashing.
        try:
            choice = int(choice_input)
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 5.\n")
            continue

        if choice == 1:
            add_contact(contacts)
        elif choice == 2:
            view_contacts(contacts)
        elif choice == 3:
            search_contact(contacts)
        elif choice == 4:
            delete_contact(contacts)
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            # Handles valid integers that are out of the 1-5 range,
            # e.g. 0 or 99.
            print("Invalid choice. Please enter a number from 1 to 5.\n")


if __name__ == "__main__":
    main()