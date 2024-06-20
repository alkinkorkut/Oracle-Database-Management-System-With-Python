import oracledb

# Helpers for working with Oracle database

# Assume that there is a table named 'users'
# with columns 'id', 'username', 'name', 'email', "salary"

USERNAME = "username"
PASSWORD = "password"
DSN = "dsn"

def get_version():
    connection = oracledb.connect(USERNAME, PASSWORD, DSN)
    print("Version of python-oracledb library: ",oracledb.version)
    print("Version of Oracle Database: ", connection.version)
    connection.close()

# CRUD Operations for users (Create, Read, Update, Delete)

def create_user(id, username, name, email, salary):
    """

    Connects to Oracle database and create a new user in the users table.
    Insert a new record with the given id, username, name, email, and salary.

    Parameters:
    id (int): User ID
    username (str): Username
    name (str): Name
    email (str): Email
    salary (float): Salary

    """
    connection = oracledb.connect(USERNAME, PASSWORD, DSN)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (id, username, name, email, salary) VALUES (:id, :username, :name, :email, :salary)",
                   id=id, username=username, name=name, email=email, salary=salary)
    connection.commit()
    cursor.close()
    connection.close()

def read_users():
    """

    Connects to the Oracle database and reads and prints all users.
    Query and retrieve all records from the users table.

    """
    connection = oracledb.connect(USERNAME, PASSWORD, DSN) 
    cursor = connection.cursor() 
    cursor.execute("SELECT * FROM users") 
    records = cursor.fetchall()
    for record in records: 
        print(record) # Print all records
    cursor.close()
    connection.close()

def update_user(id, username, name, email, salary):
    """

    Connects to Oracle database and updates the user with the given id.
    Modify the existing record with the given id, username, name, email, and salary.

    Parameters:
    id (int): User ID
    username (str): Username
    name (str): Name
    email (str): Email
    salary (float): Salary

    """
    connection = oracledb.connect(USERNAME, PASSWORD, DSN)
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET username=:username, name=:name, email=:email, salary=:salary WHERE id=:id",
                   username=username, name=name, email=email, salary=salary, id=id)
    connection.commit()
    cursor.close()
    connection.close()

def delete_user(id):
    """

    Connects to Oracle database and deletes the user with the given id.
    Remove the record with the given id from the users table.

    Parameters:
    id (int): User ID

    """
    connection = oracledb.connect(USERNAME, PASSWORD, DSN)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE id=:id", id=id)
    connection.commit()
    cursor.close()
    connection.close()

def get_user_by_id(id):
    """

    Connects to Oracle database and retrieves the user with the given id.
    Query and retrieve the record with the given id from the users table.

    Parameters:
    id (int): User ID

    Returns:
    dict: A dictionary containing the user information (id, username, name, email, salary)

    """
    connection = oracledb.connect(USERNAME, PASSWORD, DSN)
    cursor = connection.cursor()

    try: 
        cursor.execute("SELECT * FROM users WHERE id=:id", id=id)
        user = cursor.fetchone()

        if user: 
            user_dict = {
                'id': user[0],
                'username': user[1],
                'name': user[2],
                'email': user[3],
                'salary': user[4]
            }
            return user_dict
        else:
            print("User not found with ID {id}")
            return None
    
    except oracledb.DatabaseError as error:
        print("Error occurred while fetching the user:", error)
        return None

    finally:
        cursor.close()
        connection.close()

def get_user_by_username(username):
    """

    Connects to Oracle database and retrieves the user with the given username.
    Query and retrieve the record with the given username from the users table.

    Parameters:
    username (str): Username

    Returns:
    dict: A dictionary containing the user information (id, username, name, email, salary)

    """
    connection = oracledb.connect(USERNAME, PASSWORD, DSN)
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM users WHERE username=:username", username=username)
        user = cursor.fetchone()

        if user:
            user_dict = {
                'id': user[0],
                'username': user[1],
                'name': user[2],
                'email': user[3],
                'salary': user[4]
            }
            return user_dict
        else:
            print("User not found with username {username}")
            return None

    except oracledb.DatabaseError as error:
        print("Error occurred while fetching the user:", error)
        return None

    finally:
        cursor.close()
        connection.close()
