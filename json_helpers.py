import json

# Helper functions for working with JSON files

def create_user(new_user_info):
    """

    Creates a new user to the 'users.json' file.

    Parameters:
    new_user_info (dict): A dictionary containing the user information
                            (e.g., id, username, name, email, salary)

    """
    users_data = read_users()
    users_data.append(new_user_info)
    with open('users.json', 'w') as users_file:
        json.dump(users_data, users_file, indent=4)

def read_users():
    """

    Reads users from 'users.json' file and returns them as a list.

    """
    with open('users.json', 'r') as users_file:
        users_data = json.load(users_file)
    return users_data

def update_user(user_id, updated_user_info):
    """

    Updates the user with the given id in the 'users.json' file.

    Parameters:
    user_id (int): The id of the user to be updated
    updated_user_info (dict): A dictionary containing the updated user information

    """
    users_data = read_users()
    for user in users_data:
        if user['id'] == user_id:
            user.update(updated_user_info)
            break
    with open('users.json', 'w') as users_file:
        json.dump(users_data, users_file, indent=4)

def delete_user(user_id):
    """

    Deletes the user with the given id from the 'users.json' file.

    Parameters:
    user_id (int): The id of the user to be deleted

    """
    users_data = read_users()
    users_data = [user for user in users_data if user['id'] != user_id]
    with open('users.json', 'w') as users_file:
        json.dump(users_data, users_file, indent=4)

def get_user_by_id(user_id):
    """

    Returns the user with the given id.

    Parameters:
    user_id (int): The id of the user to be retrieved

    """
    users_data = read_users()
    for user in users_data:
        if user['id'] == user_id:
            return user
        
def get_user_by_username(username):
    """

    Returns the user with the given username

    Parameters:
    username (str): The username of the user to be retrieved
    
    """
    users_data = read_users()
    for user in users_data:
        if user['username'] == username:
            return user
