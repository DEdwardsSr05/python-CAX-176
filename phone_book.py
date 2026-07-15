# David Edwards
# 2026-CAX-176
# July 15, 2026
# Company Directory

# phone book entries

phone_book = {
    "Bob": "555-1111",
    "Alice": "555-2222"
}

print(phone_book["Bob"])           # look up key
phone_book["Alice"] = "555-0000"   # update existing key
phone_book["David"] = "555-4321"   # add new entry

print(phone_book)