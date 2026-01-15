import os

def save_new_contact(user_contact_list):
    ''' 
    This function takes user_contact_list as a input parameter
    and adds the contact information to the contact_database.txt file.

    search_name: list
    return: None
    '''
    with open(os.path.join(os.getcwd(),"contact_database.txt"),'a+') as f_user:
        user_contact = ",".join(user_contact_list)+"\n"
        f_user.write(user_contact)

        print(f"\nNew Contact: {user_contact_list[0]} Created Successfully!")

def search_contacts_by_names(search_name):
    ''' 
    This function takes search_name as a input parameter
    and fetches the contact information from the contact_database.txt file 
    based on the name.

    search_name: String
    return: None
    '''
    with open(os.path.join(os.getcwd(),"contact_database.txt"),'r') as f_user:
        content = f_user.readlines()
        for contact in content:
            if search_name.lower() in contact.split(',')[0].lower():
                contact_data = contact.split(',')
                name = contact_data[0]
                phoneNum = contact_data[1]
                emailAddress = contact_data[2]
                group = contact_data[3]
                print(f"\nContact Name: {name}, \nEmail: {emailAddress}, \nPhone Number: {phoneNum}, \nGroup: {group}\n")

def search_contacts_by_group(search_group):
    ''' 
    This function takes search_group as a input parameter
    and fetches the contact information from the contact_database.txt file 
    based on the group name: Home or Office

    search_group: String
    return: None
    '''
    with open(os.path.join(os.getcwd(),"contact_database.txt"),'r') as f_user:
        content = f_user.readlines()
        i = 1
        print()
        for contact in content:
            if search_group.lower() in contact.split(',')[-1].lower():
                contact_data = contact.split(',')
                name = contact_data[0]
                phoneNum = contact_data[1]
                emailAddress = contact_data[2]
                group = contact_data[3]
                print(f"Contact No.:{i}, \nContact Name: {name}, \nEmail: {emailAddress}, \nPhone Number: {phoneNum}, \nGroup: {group}")
                i+=1

def delete_contact_by_phoneNumber(phoneNo):
    ''' 
    This function takes PhoneNumber as a input parameter
    and deletes the contact information from the contact_database.txt file

    phoneNo: String
    return: None
    '''
    with open(os.path.join(os.getcwd(),"contact_database.txt"),'r+') as f_user:
        content = f_user.readlines()
        new_content = []
        for contact in content:
            if str(phoneNo)!=str(contact.split(',')[1]):
                new_content.append(contact)
        with open(os.path.join(os.getcwd(),"contact_database.txt"),'w') as f_write:
            f_write.writelines(new_content)
    if len(content) > len(new_content):
        print(f"\nContact Number: {phoneNo} Deleted Successfully!")
    else:
        print(f"\nNo Such Number: {phoneNo} Exists!")

print("=========================Welcome to PyContactBook===============================")
print("=============Press 1: To Create the New Contact=================================")
print("=============Press 2: To Search the Existing Contact List by Names==============")
print("=============Press 3: To Search the Existing Contact List by Group==============")
print("=============Press 4: To Delete the Existing Contact using Phone Number ========")

user_option = int(input())

if user_option == 1:
    name = input("Enter the Contact Name: ")
    phoneNo = input("Enter the Contact Phone Number: ")
    emailAddress = input("Enter the Contact Email Address: ")
    group = input("Enter the Contact group Name - either Home or Office: ")
    user_contact_list = [name,phoneNo,emailAddress,group]
    save_new_contact(user_contact_list)
if user_option == 2:
    search_name = input("Enter the Contact Name to Search: ")
    search_contacts_by_names(search_name)
if user_option == 3:
    search_group = input("Enter the Contact Group Name to Search: ")
    search_contacts_by_group(search_group)
if user_option == 4:
    phoneNumber = str(input("Enter the Contact Phone Number to Delete: "))
    delete_contact_by_phoneNumber(phoneNumber)