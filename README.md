# AirBnB Clone

## Project Overview

The AirBnB Clone is a web-based project designed to replicate the functionality of the AirBnB platform. It includes features such as user management, property listings, and booking management. The project uses Python and various web technologies, and it's structured to provide a robust foundation for further development and customization.

### Key Features:
- Create new objects (e.g., `User`, `Place`, `State`, etc.).
- Retrieve object details by ID.
- Update object attributes.
- Destroy objects by ID.
- Store and load object data in/from JSON files.

## Command Interpreter

The **HBNB** command interpreter provides a set of commands to interact with the object models and storage. These commands allow users to perform actions such as creating new instances of classes, viewing or updating instance attributes, or deleting instances.

### How to Start the Command Interpreter

To start the command interpreter, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/alu-AirBnB_clone.git
   ```
2. Navigate to the repository directory:
   ```bash
   cd alu-AirBnB_clone
   ```
3. Start the command interpreter:
   ```bash
   ./console.py
   ```

### How to Use the Command Interpreter

Once the command interpreter is running, you will see the prompt `hbnb`. You can type commands to interact with the application. Here's a list of available commands and how to use them:

#### Common Commands

- `quit`: Exits the command interpreter.
    ```bash
    hbnb> quit
    ```

- `EOF`: Exits the command interpreter by handling the EOF signal (`Ctrl + D`).
    ```bash
    hbnb> EOF
    ```

- `create <class>`: Creates a new instance of the specified class and prints the ID.
    ```bash
    hbnb> create BaseModel
    ```

- `show <class> <id>`: Displays the string representation of an instance based on class name and instance ID.
    ```bash
    hbnb> show BaseModel 1234-1234-1234
    ```

- `destroy <class> <id>`: Deletes an instance based on class name and ID.
    ```bash
    hbnb> destroy BaseModel 1234-1234-1234
    ```

- `all [<class>]`: Displays all string representations of instances, or instances of a specific class (if a class is provided).
    ```bash
    hbnb> all
    hbnb> all User
    ```

- `update <class> <id> <attribute name> <attribute value>`: Updates the attributes of an instance based on the class name, ID, attribute name, and value.
    ```bash
    hbnb> update BaseModel 1234-1234-1234 name "New Name"
    hbnb> update BaseModel 1234-1234-1234 age 30
    ```

### Examples of Usage

1. **Creating an instance**:
    ```bash
    hbnb> create User
    4f3e3f0b-1a4c-49fb-8a8a-b92820af109e
    ```

2. **Showing an instance**:
    ```bash
    hbnb> show User 4f3e3f0b-1a4c-49fb-8a8a-b92820af109e
    [User] (4f3e3f0b-1a4c-49fb-8a8a-b92820af109e) {'id': '4f3e3f0b-1a4c-49fb-8a8a-b92820af109e', 'created_at': '2024-09-14T12:00:00', 'updated_at': '2024-09-14T12:00:00'}
    ```

3. **Destroying an instance**:
    ```bash
    hbnb> destroy User 4f3e3f0b-1a4c-49fb-8a8a-b92820af109e
    ```

4. **Listing all instances**:
    ```bash
    hbnb> all
    ```

5. **Updating an instance**:
    ```bash
    hbnb> update User 4f3e3f0b-1a4c-49fb-8a8a-b92820af109e email "user@example.com"
    ```

## Files

- `console.py`: The command interpreter.
- `models/`: Directory containing all class definitions and storage methods.

## Installation

Clone the repository and ensure you have Python 3.x installed. You can run the command interpreter directly from the terminal.

---
