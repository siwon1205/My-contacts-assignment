
def newContact(name, phone, email):
    return {
        "name": name,
        "phone": phone,
        "email": email
    }

def LinearSearch(contacts, name):
    for i in range(len(contacts)):
        if contacts[i]["name"] == name:
            return i
    return - 1

contacts = []
contacts.append(newContact("Makima", "123", "makim@gmail.com"))
contacts.append(newContact("Power", "789", "power@gmail.com"))
contacts.append(newContact("Denji", "456", "denji@gmail.com"))

loop = True
while loop:

    
    #Print main menu
    print("Main Menu")
    print("1. Display Contact Names")
    print("2. Search for Contact")
    print("3. Edit Contact")
    print("4. New Contact")
    print("5. Remove Contact")
    print("6. Exit")

    #Menu Selection
    select = input ("Enter Selection (1-6): ")

    #Selection Results
    if select == "1":
        print("Display Contact Names")
        for contact in contacts:
         print(contact["name"])
        
    elif select == "2":  #find way to end loop
        print("Search for Contact")
        nameOf = input("what is the contact name: ")
        for contact in contacts:
            if contact['name'] == nameOf:
                print(f"{contact['name']}   {contact['email']}   {contact['phone']}")
                break
            else:
                print("Contact not found")

    elif select == "3":
        print("edit the contact")
        newcontact = input("Please enter a contact to edit: ")
        result = LinearSearch(contacts, newcontact)
        if(result == -1):
            print("contact not found")
        else:
            print("type new information for contact")
            newName = input("type new name: ")
            contacts[result]['name'] = newName
            newEmail = input("type new email: ")
            contacts[result]['email'] = newEmail
            newPhone = input("type new phonenumber: ")
            contacts[result]['phone'] = newPhone
      
    elif select == "4":
        print("New Contact")
        addname = input("Enter a new contact to add: ")
        result = LinearSearch(contacts, addname)
        if(result == -1):
            print("add the following data: phone, email")
            addname = input("add name: ")
            addemail = input("add email: ")
            addphone = input("add phone number: ")
            contacts.append(newContact(addname, addphone, addemail))
        else:
            print("contact already exists")

    elif select == "5":
        print("Remove Contact")
        byebye = input("Please enter a contact to remove: ")
        result = LinearSearch(contacts, byebye)
        if(result == -1):
            print("contact does not exist")
        else:
            contacts.pop(result)
            print("contact has been removed")

    elif select == "6":
        print ("EXIT")
        loop = False



        