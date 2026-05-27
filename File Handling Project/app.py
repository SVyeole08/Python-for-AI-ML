from pathlib import Path
import os

def createFile():
    name = input("Enter the file name you want to create:-")
    path = Path(name)
    try:
        if not path.exists():
            with open(path,"w") as fs:
                data = input("Enter the content you want to put in the created file:-")
                fs.write(data)
            print("File created succesfully")
        else:print(f"{path} already exists try to make different.")
    except Exception as err:
        print(f"An error occured due to {err}")

def readFile():
    name = input("Enter the file name you want to read:-")
    path = Path(name)
    try:
        if path.exists():
            with open(path,"r") as fs:
                content = fs.read()
                print(content)
            print("File read successfully")
        else:print(f"{path} does not exists.")
    except Exception as err:
        print("An error occured due to {err}")

def updateFile():
    name = input("Enter the file name you want to update:-")
    path = Path(name)
    try: 
        if path.exists():
            print("1. Rename the file")
            print("2. Append content in the file")
            print("3. Overwrite content in the file")

            choice = int(input("Enter your choice:-"))
            if choice == 1:
                new_name = input("Enter the new name of the file:-")
                new_path = Path(new_name)
                if not new_path.exists():
                    path.rename(new_path)
                    print(f"File name changed to {new_name}")
                else : print(f"{new_name} already exists try other name")
            elif choice == 2:
                with open(path,"a") as fs:
                    data = input("Enter the data you want to append:-")
                    fs.write(data)
                print("Data appended successfully.")
            elif choice == 3:
                with open(path,"w") as fs:
                    data = input("Enter the data you want to overwrite:-")
                    fs.write(data)
                print("Data overwrote successfully.")
            else: print("Plese enter right choice.")
    except Exception as err:
        print(f"An error occured due to {err}")

def deleteFile():
    name = input("Enter the file name you want to delete:-")
    path =  Path(name)
    try:
        if path.exists():
            path.unlink()
            print(f"{name} deleted successfully.")
        else : print(f"{name} does not exists.")
    except Exception as err:
        print(f"An error occured due to {err}")
        
print("Enter 1 to Create a file")
print("Enter 2 to Read a file")
print("Enter 3 to Update a file")
print("Enter 4 to Delete a file")

a = int(input("Enter you choice:-"))
if a == 1:
    createFile()
elif a == 2:
    readFile()
elif a == 3:
    updateFile()
elif a == 4:
    deleteFile()
else : print("Please enter right choice")