from handler import handler_dict
from parser_gear import parser_gear_user_input

def user_name_input():
    name_input = input("Hello! What is your name?\nPlease enter: ")
    print(f"\n{name_input.lower().capitalize()}, nice to meet you. let's start.\n")

def main():
    user_name_input()
    print("""You can use the following commands for your contact list:
    - add name number - it's simple, to add new contact to your contact list;
    - change name new-number - to set up new number for contact with this name (if exist);
    - delete name - to delete the contact with this name from contact list (if exist);
    - phone name - to see the phone number for this name (if exist);
    - show all - to see all contacts in your contact list (if you have added at least 1);
    - good bye / close / exit - to finish work and close session;
    """)
    while True:
        user_input = input("Please enter command: ")
        result = parser_gear_user_input(user_input=user_input)
        if len(result) != 2:
            print(result)
            continue
        command, arguments = result
        command_handler = handler_dict.get(command)
        try:
            command_response = command_handler(*arguments)
            print(command_response)
        except SystemExit as err:
            print(str(err))
            break


if __name__ == "__main__":
    main()