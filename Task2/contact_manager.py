# contact_manager.py

import json
import os

FILE = "contacts.json"

def load_contacts():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(name, phone):
    contacts = load_contacts()
    contacts[name] = phone
    save_contacts(contacts)
    print(f"Contact {name} added successfully.")

def update_contact(name, phone):
    contacts = load_contacts()
    if name in contacts:
        contacts[name] = phone
        save_contacts(contacts)
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} does not exist.")

def display_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

# Example usage
if __name__ == "__main__":
    add_contact("Hizar", "03499224226")
    update_contact("Hizar", "03490000000")
    display_contacts()
