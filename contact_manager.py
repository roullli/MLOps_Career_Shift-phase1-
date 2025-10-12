from pathlib import Path

contacts_dict = {}


def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    contacts_dict[name] = phone


def search_contact():
    name_search = input("Enter the name you want to get the phone number for:")
    print(f"{name_search}'s number is: {contacts_dict[name_search]}")


def delete_contact():
    name_delete = input(
        "Enter the name for a person you want to delete his/her number:"
    )
    del contacts_dict[name_delete]


def list_all():
    for key, value in contacts_dict.items():
        print(f"{key}: {value}")


def save_to_file():
    path = Path("files") / "contacts.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="UTF-8") as file:
        for key, value in contacts_dict.items():
            file.write(f"{key}: {value} \n")

def load_from_file():
    with open('files/contacts.txt', 'r') as file:
        print(file.read())

while True:
    user_selection = input(
        """
    Select one of the following actions:
    1. Add a contact
    2. Search a contact
    3. Delete a contact
    4. List all contacts
    5. Save contacts to a file
    6. Load contacts the file
    7. Exit
    Enter the number: 
    """
    )
    load_from_file()
