
import csv

# Create contacts.csv
contacts = [
    ["Aman", "9876543210"],
    ["Ankit", "9876543211"],
    ["Rahul", "9876543212"],
    ["Priya", "9876543213"],
    ["Arjun", "9876543214"]
]

with open("contacts.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Phone"])
    writer.writerows(contacts)


# Read contacts using DictReader
with open("contacts.csv", "r") as file:
    reader = csv.DictReader(file)

    print("Contacts starting with A:")

    for contact in reader:
        if contact["Name"].startswith("A"):
            print(contact["Name"], "-", contact["Phone"])
