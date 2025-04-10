# 1. Create a list named 'contacts' with at least 4 contacts.
# Each contact will be represented as a list with name, phone, and email.

contacts = [
    ['Alice', '555-1234', 'alice@email.com'],
    ['Bob', '555-5678', 'bob@email.com'],
    ['Charlie', '555-8765', 'charlie@email.com'],
    ['Diana', '555-4321', 'diana@email.com']
]

# 2. Print the details of the second contact.
# Output will be: ['Bob', '555-5678', 'bob@email.com']
print(contacts[1])
# 3. Update the phone number of the third contact.
contacts[2][1] = "555-8888"
# 4. Add a new contact to the list.
contacts.append(["Eli","555-6767","Eli@gmail.com"])
# 5. Print the updated contact list.
print(contacts)