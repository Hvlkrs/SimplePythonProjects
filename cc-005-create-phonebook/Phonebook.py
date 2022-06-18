



#print ("Welcome to the phonebook application!")
#print ("Select operation on Phonebook App!")
#print ("1. Find phone number")
#print ("2. Insert a phone number")
#print ("3. Delete a person from the phonebook")
#print ("4. Terminate the program")

def welcome():
    entry = int(input ("Select operation on Phonebook App (1/2/3/4/5) : "))

    return entry

def phonebook():
    contact = {}

    while True:
        entry = welcome()

        if entry == 1:

            if bool(contact) != False:
                for k, v in contact.items():
                    print(k, '-->', v)
            else:
                print("You have an empty phonebook. Go back to menu to add new contact")
        
        elif entry == 2:
            phone_number = input('Please enter a number: ')
            contact_name = input('Please enter a contact name: ')
            if phone_number not in contact.items():
                contact.update({contact_name:phone_number})

                print('Contact successfully saved')
                print('Your updated phonebook is shown below: ')
                for k,v in contact.items():
                    print(k, '-->', v)
            else:
                print('That contact already exist in your Phonebook')

        elif entry == 3:
            name = input('Enter the name of contact details you wish to view: ')
            if name in contact:
                print('The contact is',name,':',contact[name])

            else:
                print('That contact exist in your Phonebook')

        elif entry == 4:
            name = input('Enter the name of contact you wish to delete: ')
            
            if name in contact:
                print('The contact is',name,':',contact[name])
            else:
                print('That contact does not exist.')

            confirm = input('Are you wish to delete this contact? Yes/No: ')
            if confirm.capitalize() == 'Yes':
                contact.pop(name,None)
                for k, v in contact.items():
                    print('Your updated Phonebook is shown below: ')
                    print(k, '-->', v)
            else:
                print('Return to main menu')
        

        elif entry == 5:
            print('Thanx for using Phonebook')
            break
        else:
            print('Incorrect entry')