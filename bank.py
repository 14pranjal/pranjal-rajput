import json
from pathlib import Path
import random
import string


class bank:
    data = []
    __database = "data.json"

    try:
        if Path(__database).exists():
            with open(__database) as fs:
                data = json.load(fs)
    except Exception as err:
        print(f"an error occured as{err}")


    @classmethod
    def __updatedata(cls):
        with open(cls.__database, "w") as fs:
            fs.write(json.dumps(cls.data))
    

    @classmethod
    def __Generate_Account_number(cls):
        alpha = random.choices(string.ascii_letters,k=5)
        numbers = random.choices(string.digits, k=5)
        id = alpha + numbers
        random.shuffle(id)
        return "".join(id)


    def create_Account(self):
        info = {
            "Name":input("tell your Name:- "),
            "Age":int(input("tell your Age:- ")), 
            "Email":input("tell your Email:- "),   
            "AccountNo": self.__Generate_Account_number(),
            "PHONE":int(input("tell your PHONE NUMBER:- ")),  
            "GENDER":input("tell your GENDER:- "), 
            "Pin":int(input("tell your Pin:- ")),
            "Balance":0 
        }
        if info['Age'] < 18:
           print("sorry you cannot create Account")

        elif len(str(info["PHONE"])) != 10:
           print("invalid phone number or Pin")
        
        elif not len(str(info["Pin"])) == 4:
            print("invalid Pin")

        else :
            bank.data.append(info)
            bank.__updatedata()
  
        print(f"your Account no is {info['AccountNo']}, done")

    def deposit_money(self):
        Account_no = input("tell your Account no:- ")
        pin = int(input("tell your pin :- "))

        user_data = [i for i in bank.data if i["AccountNo"].lower() == Account_no.lower() and i["Pin"] == pin]

        if not user_data:
            print("no such user found")
        else:
            amount = int(input("how much you want to deposit"))

            if amount < 0:
                print("sorry you cannot deposit a negative amount")
            elif amount > 20000:
                print("sorry you cannot deposit more than 20000rs")
            else:
                user_data[0]['Balance'] += amount
                bank.__updatedata()
                print("amount deposited successfully")

    def withdraw_money(self):
        Account_no = input("tell your account number:- ")
        pin = int(input("tell your Pin :- "))

        user_data = [i for i in bank.data if i["AccountNo"] == Account_no and i['Pin'] == pin]

        if not user_data:
            print("no such user found")
        else:
            amount = int(input("how much you want to withdraw:- "))
            if amount > 20000:
                print("sorry you cannot withdraw more than 20000rs")
            elif amount > user_data[0]["Balance"]:
                print("insufficient balance")
            else:
                user_data[0]['Balance'] -= amount
                bank.__updatedata()
                print("amount withdrawn successfully")


    def Account_detail(self):
        Account_no = input("tell your Account number:- ")
        pin = int(input("tell your Pin :- "))


        user_data = [i for i in bank.data if i["AccountNo"] == Account_no and i['Pin'] == pin]
 
        if not user_data:
            print("no such user found")
        else:
            for i  in user_data[0]:
              print(f"{i} : {user_data[0][i]}")

    def update_detail(self):
        account_no = input("tell your account number:- ")
        pin = int(input("tell your pin :- "))

        user_data = [i for i in bank.data if i["AccountNo"] == account_no and i['Pin'] == pin]


        if not user_data:
             print("no such user found")
        else:
            print("you cannot change your account number ")
            print("now update your detail")
            newdata = {
                "Name":input("tell your Name:- "),
                "Age":input("tell your Age:- "),
                "Email":input("tell your Email:- "),
                "Phone":input("tell your Phone number"),
                "pin":input("tell your pin:- "),
            }

            if newdata['Name'] == "":
                newdata['Name'] = user_data[0]['Name']
            elif newdata['Age'] == "":
                newdata['Age'] = user_data[0]['Age']
            elif newdata['Email'] == "":
                newdata['Email'] = user_data[0]['Email']
            elif newdata['Phone'] == "":
                newdata['Phone'] = user_data[0]['Phone']
            elif newdata['pin'] == "":
                newdata['pin'] = user_data[0]['Pin'] 

            newdata["Account no."] = user_data[0]["Account no."] 
            newdata['']


    def Delete_account(self):
        account_no = input("tell your account number:- ")
        pin = int(input("tell your pin :- "))

        user_data = [i for i in bank.data if i["AccountNo"] == account_no and i['Pin'] == pin]


        if not user_data == False:
             print("no such user found") 


print(""" press the following for your task :- 
          press 1 for Creating the bank Account.
          press 2 for Depositing money in your bank Account.
          press 3 for Withdrawing the money in your bank Account.
          press 4 for Account Detail.
          press 5 for Updating Detail.
          press 6 for Deleting the Account.
       
          press 0  to Exists""")

user = bank()
check = input("tell your response:- ")

if check == "1":
   user.create_Account()

if check == "2":
    user.deposit_money()

if check == "3":
    user.withdraw_money()

if check == "4":
    user.account_detail()

if check == "5":
    user.update_detail()

if check == "6":
    user.Delete_account()
if check == "0":
    user.exists()