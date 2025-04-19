import ast

def phone_book():
    contact = input("Enter the contact:")
    user_input = ast.literal_eval(contact)
    print(user_input)
    print("What do you want to do- \n 1.Search the contact \n 2.Delete the contact \n 3.Display the contact")
    value = int(input("Choose the value:"))
    if value == 1:
        key1 =input("Enter the name you want to search:")
        if key1 in user_input:
            print(f"contact number: {user_input[key1]}")
        else:
            print("key not found!!")
    elif value == 2:
        key_delete = input("Enter the contact you want to delete:")
        if key_delete in user_input:
            del user_input[key_delete]
            print(f"Key {key_delete} is deleted")
        else:
            print("key not found!!")
    elif value == 3:
        print(f"Current Dictonary: {user_input}")
    else:
        print("Select the currect value!!")
        

phone_book()   