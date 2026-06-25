import json
from pathlib import Path

DB = Path("S:\AI ML\Python\Projects\BankManagementSystem\db.json")
data = {"accounts": []}

if Path(DB).exists():
    with open(DB, "r") as f:
        content = f.read()
        if content:
            data = json.loads(content)


def proceed():
    with open(DB, "w") as f:
        json.dump(data, f, indent=4)


def validateEmail(email):
    return "@" in email and "." in email


class Bank:
    def CreateAccount(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        mob = int(input("Enter your mobile number: "))
        email = input("Enter your email: ")
        balance = int(
            input(
                "How much money you want to deposit: (enter zero if you don't want to deposit) "
            )
        )

        if not validateEmail(email):
            print("Invalid email")
            return

        acc_no = len(data["accounts"]) + 1

        data["accounts"].append(
            {
                "acc_no": acc_no,
                "name": name,
                "age": age,
                "mob": mob,
                "email": email,
                "balance": balance,
            }
        )

        proceed()
        print(
            f"Your account is successfully created and you got assigned {acc_no} as account number and you have {balance} in your account."
        )

    def DepositeMoney(self):
        acc_no = int(input("Enter your account number: "))
        money = int(input("Enter the amount you want to deposit: "))

        for i in data["accounts"]:
            if i["acc_no"] == acc_no:
                i["balance"] += money
                proceed()
                print(
                    f"You have successfully deposited {money} in your account and your current balance is {i['balance']}."
                )
                return
            print("Please enter account number carefully.")

    def WithdrawMoney(self):
        acc_no = int(input("Enter your account number: "))
        money = int(input("Enter the amount you want to withdraw: "))

        for i in data["accounts"]:
            if i["acc_no"] == acc_no:
                if i["balance"] < money:
                    print("Insufficient balance.")
                    return
                i["balance"] -= money
                proceed()
                print(
                    f"You have successfully withdrawn {money} from your account and your current balance is {i['balance']}."
                )
                return
            else:
                print("Please enter account number carefully.")
                return

    def Details(self):
        acc_no = int(input("Enter your account number: "))

        for i in data["accounts"]:
            if i["acc_no"] == acc_no:
                print(f"Details of account number {acc_no} are as follows: ")
                print("Name: ", i["name"])
                print("Age: ", i["age"])
                print("Mobile number: ", i["mob"])
                print("Email: ", i["email"])
                return
            print("Please enter account number carefully.")

    def UpdateDetails(self):
        acc_no = int(input("Enter your account number: "))

        for i in data["accounts"]:
            if i["acc_no"] == acc_no:
                newName = input("Enter your new name: ")
                newAge = int(input("Enter your new age: "))
                newMob = int(input("Enter your new mobile number: "))
                newEmail = input("Enter your new email: ")

                if not validateEmail(newEmail):
                    print("Invalid email")
                    return

                i["name"] = newName
                i["age"] = newAge
                i["mob"] = newMob
                i["email"] = newEmail
                proceed()

                print("Your account details updated successfully.")
                return

            print("Please enter account number carefully.")

    def DeleteAccount(self):
        acc_no = int(input("Enter your account number: "))

        for i in data['accounts']:
            if i["acc_no"]==acc_no:
                data["accounts"].remove(i)
                proceed()
                print("Your account is been deleted successfully.")
                print("We are so sorrowfull to see you go!")
                return
            print("Please enter account number carefully.")

user = Bank()

print("Enter 1 for creating an account ")
print("Enter 2 for depositing money in account ")
print("Enter 3 for withdrawing money from account ")
print("Enter 4 for details of account ")
print("Enter 5 for updating details of account ")
print("Enter 6 for deleting account ")

check = int(input("Enter your choice: "))

if check == 1:
    user.CreateAccount()

if check == 2:
    user.DepositeMoney()

if check == 3:
    user.WithdrawMoney()

if check == 4:
    user.Details()

if check == 5:
    user.UpdateDetails()

if check == 6:
    user.DeleteAccount()
