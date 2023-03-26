def parser_gear_error_handler(func):

    def wrapper(user_input: str):
        try:
            return func(user_input)
        except (ValueError, KeyError, TypeError) as err:
            print("Incorrect input. \nPlease check details and enter correct command ")
            return str(err)
        
    return wrapper


def hello_parser_gear(user_input: str):
    username = user_input.lstrip("add").strip().split(" ")
    return "hello", [username]


def add_parser_gear(user_input: str):
    username, number = user_input.lstrip("add").strip().split(" ")

    if len(username) > 0 and len(number) > 0:
        username = username.capitalize()
        return "add", [username, number]
    
    raise ValueError


def change_parser_gear(user_input: str):
    username, number = user_input.lstrip("change").strip().split(" ")

    if len(username) > 0 and len(number) > 0:
        username = username.capitalize()
        return "change", [username, number]
    
    raise ValueError


def delete_parser_gear(user_input: str):
    input_list = user_input.lstrip("delete").strip().split(" ")
    username = input_list[0]

    if len(username) > 0 :
        username = username.capitalize()
        return "delete", [username]
    
    raise ValueError


def phone_parser_gear(user_input: str):
    input_list = user_input.lstrip("phone").strip().split(" ")
    username = input_list[0]

    if len(username) > 0 :
        username = username.capitalize()
        return "phone", [username]
    
    raise ValueError


def show_parser_gear(user_input: str):

    if user_input.lower().strip() == "show all":
        return "show all", []
    
    return ValueError


def exit_parser_gear(user_input: str):

    if user_input.lower().strip() == ("goodbye", "close",  "exit"):
        return "exit", []
    
    raise ValueError


parser_gears_dict = {
    "hello": hello_parser_gear,
    "add": add_parser_gear,
    "change": change_parser_gear,
    "delete": delete_parser_gear,
    "phone": phone_parser_gear,
    "goodbye": exit_parser_gear,
    "close": exit_parser_gear,
    "exit": exit_parser_gear
}


@parser_gear_error_handler
def parser_gear_user_input(user_input: str) -> tuple[str, list]:

    for command in parser_gears_dict.keys():
        normalized_input = " ".join(user_input.lower().strip().split(" "))

        if normalized_input.startswith(command):
            parser = parser_gears_dict.get(command)
            return parser(user_input=normalized_input)
        
    raise ValueError
