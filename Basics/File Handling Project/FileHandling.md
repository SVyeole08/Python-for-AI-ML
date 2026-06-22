# 📁 File Handling Project - CRUD Application

A command-line based **CRUD (Create, Read, Update, Delete)** application for file management built with Python.

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Project Structure](#project-structure)
5. [Functions](#functions)
6. [How to Use](#how-to-use)
7. [Error Handling](#error-handling)

---

## 🎯 Project Overview

This project demonstrates practical file handling operations using Python's `pathlib` library. It provides a user-friendly menu-driven interface to perform all basic file operations in a single application.

**Purpose:** Learn and practice file I/O operations with proper error handling and user input validation.

---

## ✨ Features

- ✅ **Create Files** - Create new files with custom content
- ✅ **Read Files** - Display complete file content
- ✅ **Update Files** - Three update options:
  - Rename files
  - Append content to files
  - Overwrite file content
- ✅ **Delete Files** - Remove files from the system
- ✅ **Error Handling** - Comprehensive exception handling
- ✅ **File Existence Checks** - Prevent overwriting and duplicates

---

## 🛠️ Technologies Used

- **Python 3.x**
- **pathlib** - Object-oriented filesystem paths

---

## 📁 Project Structure

```python
File Handling Project/
├── app.py              # Main application file
└── fileHandling.md          # Project documentation
```

---

## 🔧 Functions

### 1. `createFile()`

**Purpose:** Create a new file with user-provided content

**Flow:**

1. Ask user for filename
2. Check if file already exists
3. If not exists: Create file and write content
4. If exists: Show error message

**Code:**

```python
def createFile():
    name = input("Enter the file name you want to create:-")
    path = Path(name)
    try:
        if not path.exists():
            with open(path,"w") as fs:
                data = input("Enter the content...")
                fs.write(data)
            print("File created succesfully")
        else:
            print(f"{path} already exists...")
    except Exception as err:
        print(f"An error occured due to {err}")
```

**Features:**

- Prevents duplicate file creation
- Uses `with` statement for safe file handling
- Exception handling for errors

---

### 2. `readFile()`

**Purpose:** Read and display file content

**Flow:**

1. Ask user for filename
2. Check if file exists
3. If exists: Read and display content
4. If not exists: Show error message

**Code:**

```python
def readFile():
    name = input("Enter the file name you want to read:-")
    path = Path(name)
    try:
        if path.exists():
            with open(path,"r") as fs:
                content = fs.read()
                print(content)
            print("File read successfully")
        else:
            print(f"{path} does not exists.")
    except Exception as err:
        print("An error occured due to {err}")
```

**Features:**

- Validates file existence
- Displays complete file content
- Safe file handling with context manager

---

### 3. `updateFile()`

**Purpose:** Update files with three options

**Options:**

1. **Rename File** - Change filename
2. **Append Content** - Add to existing content
3. **Overwrite Content** - Replace entire content

**Flow:**

1. Ask for filename
2. Check if file exists
3. Display 3 update options
4. Execute selected operation

**Code - Option 1 (Rename):**

```python
if choice == 1:
    new_name = input("Enter new name:-")
    new_path = Path(new_name)
    if not new_path.exists():
        path.rename(new_path)
        print(f"File renamed to {new_name}")
    else:
        print(f"{new_name} already exists")
```

**Code - Option 2 (Append):**

```python
elif choice == 2:
    with open(path,"a") as fs:
        data = input("Enter data to append:-")
        fs.write(data)
    print("Data appended successfully.")
```

**Code - Option 3 (Overwrite):**

```python
elif choice == 3:
    with open(path,"w") as fs:
        data = input("Enter data to overwrite:-")
        fs.write(data)
    print("Data overwrote successfully.")
```

**Features:**

- Multiple operations in one function
- Prevents overwriting existing files
- Append and overwrite operations

---

### 4. `deleteFile()`

**Purpose:** Delete a file from the system

**Flow:**

1. Ask user for filename
2. Check if file exists
3. If exists: Delete file
4. If not exists: Show error message

**Code:**

```python
def deleteFile():
    name = input("Enter file name to delete:-")
    path = Path(name)
    try:
        if path.exists():
            path.unlink()
            print(f"{name} deleted successfully.")
        else:
            print(f"{name} does not exists.")
    except Exception as err:
        print(f"An error occured due to {err}")
```

**Features:**

- File existence validation
- Safe deletion using `path.unlink()`
- Exception handling

---

## 📖 How to Use

### Running the Application

1. **Start the program:**

 ```bash
   python app.py
 ```

2. **View menu options:**

```bash
  Enter 1 to Create a file
  Enter 2 to Read a file
  Enter 3 to Update a file
  Enter 4 to Delete a file
```

3. **Choose an operation:**

   ```bash
   Enter you choice:- 1
   ```

### Example Workflow

**Create a file:**

```bash
Choice: 1
Enter file name: notes.txt
Enter content: Hello World!
Output: File created succesfully
```

**Read the file:**

```bash
Choice: 2
Enter file name: notes.txt
Output: Hello World!
        File read successfully
```

**Update the file (Append):**

```bash
Choice: 3
Enter file name: notes.txt
Select option: 2
Enter data to append:  - Learning Python
Output: Data appended successfully.
```

**Delete the file:**

```bash
Choice: 4
Enter file name: notes.txt
Output: notes.txt deleted successfully.
```

---

## ⚠️ Error Handling

### Exception Types Handled

| Error             | Scenario                      | Handling                |
| ----------------- | ----------------------------- | ----------------------- |
| File Exists       | Creating duplicate file       | Prevents creation       |
| File Not Found    | Reading/updating non-existent | Shows error message     |
| Permission Denied | No access to file             | Catches with try/except |
| Invalid Operation | Wrong choice input            | Shows options again     |

### Try/Except Implementation

All functions use try/except blocks:

```python
try:
    # File operation code
    ...
except Exception as err:
    print(f"An error occured due to {err}")
```

---

## 🔑 Key Concepts Used

### 1. **pathlib.Path**

- Object-oriented approach to filesystem paths
- Methods:
  - `path.exists()` - Check if file exists
  - `path.rename()` - Rename file
  - `path.unlink()` - Delete file

### 2. **File Modes**

- `"r"` - Read mode
- `"w"` - Write mode (overwrites)
- `"a"` - Append mode

### 3. **Context Managers**

- `with open()` - Auto-closes file
- Ensures file closure even on errors

### 4. **User Input Validation**

- Check file existence before operations
- Prevent duplicate file creation
- Validate user choices

---

## 🚀 Learning Outcomes

By working on this project, you learned:

- ✅ File creation and writing
- ✅ File reading and content display
- ✅ File renaming operations
- ✅ Content appending and overwriting
- ✅ File deletion
- ✅ Path object usage with pathlib
- ✅ Exception handling in file operations
- ✅ Menu-driven application development
- ✅ User input validation
- ✅ Context managers for resource management

---

## 💡 Enhancements (Future Improvements)

### Possible additions

1. **File Search** - Search files by name pattern
2. **Directory Operations** - Create/manage folders
3. **File Properties** - Show file size, creation date
4. **Batch Operations** - Process multiple files
5. **File Backup** - Create file backups
6. **Search Content** - Find text within files
7. **GUI Interface** - Add graphical user interface
8. **Logging** - Record all operations

---

## 📝 Summary

This **File Handling CRUD Project** is a practical demonstration of:

- Core file I/O operations
- Error handling best practices
- Pathlib library usage
- User-friendly interface design
- Python exception handling

Perfect for beginners learning file management in Python!

---

## 🎓 Concepts Reinforced

| Concept            | Usage                        |
| ------------------ | ---------------------------- |
| File Operations    | Create, Read, Update, Delete |
| pathlib            | Path object manipulation     |
| Exception Handling | Try/except blocks            |
| Context Managers   | with statement               |
| User Input         | input() function             |
| Conditional Logic  | if/elif/else statements      |
| Functions          | Modular code organization    |

---

**Created as part of Python learning journey** 🐍
