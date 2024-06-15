import json_helpers as jh # Import helper functions working with JSON
import oracle_db_helpers as db # Import helper functions working with Oracle DB 

CONNECT_TO_DATABASE = False

def main():

    user_info_to_manipulate = {
            'id': 4,
            'username': 'example_username',
            'name': 'example_name',
            'email': 'exampleName.exampleSurname@example.com',
            'salary': 9000
    }

    if CONNECT_TO_DATABASE: # Connect to database and perform CRUD operations
        
        crud_operation = 'None'

        if crud_operation == 'CREATE_USER':
            db.create_user(user_info_to_manipulate['id'], user_info_to_manipulate['username'], user_info_to_manipulate['name'], 
                           user_info_to_manipulate['email'], user_info_to_manipulate['salary'])
        elif crud_operation == 'READ_USERS':
            db.read_users()
        elif crud_operation == 'UPDATE_USER':
            db.update_user(user_info_to_manipulate['id'], user_info_to_manipulate['username'], user_info_to_manipulate['name'], 
                           user_info_to_manipulate['email'], user_info_to_manipulate['salary'])
        elif crud_operation == 'DELETE_USER':
            db.delete_user(user_info_to_manipulate['id'])
        elif crud_operation == 'GET_USER_BY_ID':
            print(db.get_user_by_id(user_info_to_manipulate['id']))
        elif crud_operation == 'GET_USER_BY_USERNAME':
            print(db.get_user_by_username(user_info_to_manipulate['username']))
        else:
            print('Invalid CRUD operation')
        

    else: # Read from JSON file

        operation = 'None'

        if operation == 'CREATE_USER':
            jh.create_user(user_info_to_manipulate)
        elif operation == 'READ_USERS':
            print(jh.read_users())
        elif operation == 'UPDATE_USER':
            jh.update_user(user_info_to_manipulate['id'], user_info_to_manipulate)
        elif operation == 'DELETE_USER':
            jh.delete_user(user_info_to_manipulate['id'])
        elif operation == 'GET_USER_BY_ID':
            print(jh.get_user_by_id(user_info_to_manipulate['id']))
        elif operation == 'GET_USER_BY_USERNAME':
            print(jh.get_user_by_username(user_info_to_manipulate['username']))
        else:
            print('Invalid operation')
        
if __name__ == "__main__":
    main()

