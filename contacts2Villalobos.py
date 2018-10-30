#!/usr/bin/env python
#Virginia Villalobos
#October 30, 2018
#Mod8: handling exceptions
"""
This program will keep track of a users contacts, allowing the user to list, view, add, and delete contacts.
"""
import csv
import sys

FILEN = "contacts.csv"

def write(contacts):
    """
    The write() function accepts the contacts array as an argument and uses the contacts array to update the contacts.csv file with any additions or deletions
    """
    with open(FILEN, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)


def read():
    """
    The read() function reads the information from the contacts.csv file and formats it into a 2 dimensional array which is returned as contacts
    """
    contacts = []
    try:
        with open(FILEN, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        print("File not found. New file created")
    except OSError as e:
        print(type(e), e)
        sys.exit()
    except Exception as i:
        print(type(i), i)
        sys.exit()

    return contacts

def display_title():
    """
    The display_title() function will display the title "Contact Manager"
    """
    print("Contact Manager")
    print()

def display_menu():
    """
    The display_menu() function will display the menu and describe what each command will do
    """
    print("COMMAND MENU")
    print("list - display all contacts")
    print("view - view all contacts")
    print("add - add a contact")
    print("del - delete a contact")
    print("exit - exit program")
    print()

def list(contacts):
    """
    The list() function accepts the contacts array as an argument and will list the contact names in an ordered list
    """
    if len(contacts) == 0:
        print("File empty. There are curently no contacts.")
        print()
    else:
        for i in range(len(contacts)):
            contact = contacts[i][0]
            print(str(i + 1) + ". " + contact)
        print()

def view(contacts):
    """
    The view()  function accepts the contacts array as an argument and will list a specific contacts name, email, and phone number
    """
    while True:
        try:
            number = int(input("Number: "))
            break
        except ValueError:
            print("Please enter a whole number.")

    number = validate(contacts, number)

    number -= 1
    print("Name: ", contacts[number][0])
    print("Email: ", contacts[number][1])
    print("Number: ", contacts[number][2])
    print()

def add(contacts):
    """
    The add() function accepts the contacts array as an argument and will add a contacts name, email, and phone number to the contacts.csv file
    """
    name = input("Name: ")
    email = input("Email: ")
    number = input("Number: ")

    index = len(contacts)
    contacts.append([name, email, number])

    write(contacts)

    print(name, " was added.")
    print()

def deleteItem(contacts):
    """
    The deleteItem() function accepts the contacts array as an argument and will delete a contacts name, email, and phone number from the contacts.csv file
    """
    while True:
        try:
            number = int(input("Number: "))
            break
        except ValueError:
            print("Please enter a whole number.")

    number = validate(contacts, number)
    print(contacts[number-1][0] + " was deleted.")
    contacts.pop(number-1)
    write(contacts)
    print()

def validate(contacts, number):
    """
    The validate() function accepts the contacts array and number as arguments and checks to see if the number inputted is in the range of the contacts array. It returns a number inputted by the user within that range.
    """
    while number<1 or number>len(contacts):
        print()
        print("Please enter a number from 1 to ", len(contacts))
        number = int(input("Number: "))
    return number

def main():
    """
    The main() function is where the command entered is evaluated and validated. The main() function calls the appropriate function.
    """
    contacts = read()
    display_title()
    display_menu()

    command = input("Command: ")
    while command.lower() != "exit":
        if command.lower() == "list":
            list(contacts)
        elif command.lower() == "view":
            view(contacts)
        elif command.lower() == "add":
            add(contacts)
        elif command.lower() == "del":
            deleteItem(contacts)
        else:
            print()
            print("Please enter a valid command.\n")
            display_menu()

        command = input("Command: ")

    print("Bye!")

if __name__=="__main__":
    main()
