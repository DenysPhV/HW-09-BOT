from contact_list import contact_list


def command_error_handler(func):

    def wrapper(*args):
        try:
            return func(*args)
        except (ValueError, KeyError, Exception) as err:
            return str(err)

    return wrapper


def contact_valid(username: str):
    if contact_list.get(username) is not None:
        return True
    return False


def phone_valid(number: str):
    phone_number_in_digital = (number.strip().removeprefix("+").replace("(","").replace(")","").replace("-","").replace(" ",""))
    
    if phone_number_in_digital.isdigit() and phone_number_in_digital.startswith("380") and len(phone_number_in_digital) == 12:
        return True
    
    return False


@command_error_handler
def hello_handler(username):
    return f"Hello {username}, how can I help you?"


@command_error_handler
def add_handler(username: str, number: str):
    if contact_valid(username):
        raise ValueError(f"Number with name '{username}' already exist in contact list")
    else:
        if phone_valid(number):
           contact_list[username] = number
           return f"Contact with name '{username}' and number '{number}' was added successfully to contact list"
        return f"Entered '{number}' is not a phone number.\nPlease use correct: start with '+380', 12 digits"


@command_error_handler
def change_handler(username: str, number: str):

    if contact_valid(username):

        if phone_valid(number):
            contact_list[username] = number
            return f"Number for contact '{username}' was changed successfully to '{number}'"
        
        return f"Entered '{number}' is not a phone number.\nPlease use correct: start with '380', 12 digits"
    
    raise ValueError(f"Number for contact '{username}' does not exist in contact list. Please add it.")


@command_error_handler
def delete_handler(username: str):

    if username in contact_list.keys():
        contact_list.pop(username)
        return f"Contact '{username}' was deleted successfully from your contact list"
    
    raise ValueError(f"Contact with name '{username}' does not exist in contact list.")


@command_error_handler
def phone_handler(username: str):
    
    if contact_valid(username):
        phone_number = contact_list.get(username)
        return f"Phone number of contact '{username}' is: '{phone_number}'"
    
    raise ValueError(f"Number is missed for the contact with name '{username}'")
    

@command_error_handler
def show_all_handler():

    if len(contact_list) == 0:
        return "Your contact list is empty yet. Please add new contacts."
    
    first_string ="Your contact list has the following contacts:\n"
    contact_lines = "\n".join(f"Name: {username}; Phone number: {number};" for (username, number) in contact_list.items())
    return first_string + contact_lines

@command_error_handler 
def exit_handler():
    raise SystemExit("\nThank you for cooperation. Good bye!\nSee you later. Stay safe.\n")

handler_dict = {
    "hello": hello_handler,
    "add": add_handler,
    "change": change_handler,
    "delete": delete_handler,
    "phone": phone_handler,
    "show all": show_all_handler,
    "good bye": exit_handler,
    "close": exit_handler,
    "exit": exit_handler,
}
