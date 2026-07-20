contact = {}
def ShowFuntion():
    print(contact.items)
    print("name \t phon")
    for kye in contact:
        print("{} \n {}".format(kye,contact.get(kye)))    
while True:
    choice = int(input("1.Add new contact:\n" 
                       "2.Search the contact:\n"
                       "3.Desplay the contact:\n"
                       "4.Delete the contact:\n"
                       "5.Edit the contact:\n"
                       "6.Exit\n"
                       "Please write a number between 1 - 6:"))
    if choice == 1:
        name = input("Add your contact name:")
        phon = input("Add yorr contact number:")
        contact[name] = phon
    elif choice == 2:
        Contactname = input("Search the contact:")
        if Contactname in contact:
            print(Contactname,"The contact number is:",contact[Contactname])
        else:
            print('This contact is not found')
    elif choice == 3:
        if not contact:
            print("This contact book is empty..!")
        else:
            ShowFuntion()
    elif choice == 4:
        Editcontact = input("Edit your contact:")
        if Editcontact in contact:
            phon = input("Edit your phon: ")
            contact[Editcontact] = phon
            print("Phon update successfully..!")
            ShowFuntion()
        else:
            print("Name is not found ")
    elif choice == 5:
        Deletecontact = input("Whice contact do you want  to delete? ")
        if Deletecontact in contact:
             Sure = input("Are you sure to delete this contact? [y/n]")
             if Sure == "Y" or Sure == "y":
                contact.pop(Deletecontact)
                ShowFuntion()
        else:
            print("This name is not found")
    else:
        break