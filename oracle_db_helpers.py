import oracledb

# Helpers for working with Oracle database

# Assume that there is a table named 'users'
# with columns 'id', 'username', 'name', 'email', "salary"

USERNAME = "username"
PASSWORD = "password"
DSN = "dsn"

# A simple example of a transaction 
def update_salary(id, salary):
    """

    Update the salary of a user with the given id.

    Parameters:
    id (int): User ID
    salary (float): New salary value

    """
    connection = oracledb.connect(USERNAME, PASSWORD, DSN)
    cursor = connection.cursor()

    try: 
        # Fetch the current salary in case of logging purposes
        cursor.execute("SELECT salary FROM users WHERE id=:id", {"id": id})
        current_salary = cursor.fetchone()[0]

        # Update the salary
        cursor.execute("UPDATE users SET salary=:salary WHERE id=:id", {"salary": salary, "id": id})

        # Savepoint before committing
        savepoint = connection.savepoint("SavepointBeforeCommit")

        # A condition to check if the new salary is lower than the current salary
        if salary < current_salary:
            # If the new salary is lower than current salary, raise an exception
            raise ValueError("New salary cannot be lower than the current salary")

        # Commit the transaction
        connection.commit()
        print(f"Transaction committed successfully. Salary updated for user {id} with the value of {salary}.")

    except ValueError as error:
        print("Value error occurred while updating the salary:", error)
        connection.rollback(savepoint)
        print("Transaction rolled back to savepoint due to value error.")

    except oracledb.DatabaseError as error:
        print("Database error occurred while updating the salary:", error)
        connection.rollback()
        print("Transaction rolled back due to database error.")

    finally: 
        cursor.close()
        connection.close()
        

def is_connection_healthy(connection):
    """

    This function checks and returns a boolean value indicating whether the health status of connection.
    If False, a new connection should be established. 
    In order to fully check a connection's health, Connection.ping() should be used. It performs a round-trip to the database.

    Parameters:
    connection (oracledb.Connection): An Oracle database connection object

    """
    if connection.is_healthy():
        print("Connection is healthy")
    else:
        print("Connection is not healthy. Unstable connection. Please check the database and network settings.")

def get_version():
    """

    Prints the version of the python-oracledb library and the Oracle Database version.

    """
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
    cursor.execute("""
                    INSERT INTO users (id, username, name, email, salary) 
                    VALUES (:id, :username, :name, :email, :salary)
                    """, {"id": id, "username": username, "name": name, "email": email, "salary": salary})
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
    cursor.execute("""
                    UPDATE users 
                    SET username=:username, name=:name, email=:email, salary=:salary 
                    WHERE id=:id
                    """, {"username": username, "name": name, "email": email, "salary": salary, "id": id})
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
    cursor.execute("DELETE FROM users WHERE id=:id", {"id": id})
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
        cursor.execute("SELECT * FROM users WHERE id=:id", {"id": id})
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
        cursor.execute("SELECT * FROM users WHERE username=:username", {"username": username})
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
