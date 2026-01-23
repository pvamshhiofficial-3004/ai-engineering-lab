import os
from datetime import datetime as dt

class UserLoginInterFace():
    def __init__(self, users_info_file_name, users_statuses):
        self.users_info_file_name = users_info_file_name
        self.users_statuses = users_statuses
    def user_sign_up(self, user_name, password):
        with open(os.path.join(os.getcwd(), self.users_info_file_name), 'a+') as f:
            file_content = user_name + "," + password + "\n"
            f.write(file_content)
        print("SignUp Completed Successfully!")
    def user_log_in(self, user_name, password):
        login_status = False
        with open(os.path.join(os.getcwd(), self.users_info_file_name), 'r') as f:
            file_content = f.readlines()
        for file in file_content:
            if (file.split(',')[0] == user_name) and (file.split(',')[-1].split('\n')[0] == password):
                login_status = True
                break
            else:
                login_status = False
                
        if login_status == True:
            print("Login Successful!\n")
        else:
            print("Login Failed, Please check your user_name / password!")
                
        if login_status == True:
            print(f"Hey {user_name}! Welcome to Facebook.")
            print("==========Press 1: To Post the Status===========")
            print("==========Press 2: To See All the Posts=========")
            print("\n")
            post_user_input = int(input("Enter you choice: "))
            if post_user_input == 1:
                status_msg = input("Post Something Interesting: ")
                self.post_status(status_msg, user_name)
            elif post_user_input == 2:
                self.show_all_posts()
            
    def post_status(self, status_msg, user_name):
        with open(os.path.join(os.getcwd(), self.users_statuses), 'a+') as f:
            user_status_msg = f"\n{str(dt.now())[:-7]}|{user_name}|{status_msg}"
            f.write(user_status_msg)
            
    def show_all_posts(self):
        with open(os.path.join(os.getcwd(), self.users_statuses), 'r') as f:
            file_content = f.readlines()
            
            print("Facebook Posts : ")
            
            for file in file_content:
                print(f"[{file.split("|")[0]}]")
                print(f"{file.split("|")[1]}: {file.split("|")[2]}")

print("============================Welcome to Facebook====================================")
print("============================Press 1: For SignUp====================================")
print("============================Press 2: For Login=====================================")

user_input = int(input("Press 1 - If your a First Time user for SignUp else, Press 2 for Login"))
UserClassObject = UserLoginInterFace("user_login_info.txt","user_statuses.txt")
if user_input == 1:
    user_name = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    UserClassObject.user_sign_up(user_name, password)    
    
    print("Enter your credentials to Login: ")
    user_name = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    login_status = UserClassObject.user_log_in(user_name, password)
    
elif user_input == 2:
    user_name = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    login_status = UserClassObject.user_log_in(user_name, password)
else:
    print("InValid Option, Please Try Again!")