import functools
CONTACTS_ARRAY = {}

def error_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = False

        try:
            result = func(*args, **kwargs)
        except TypeError:
            print("""You have not entered all data!!!
--------------------------------------------------------------------------------------------------
for adding new phone number please input:   add name tel.      (example: add Denys 345-45-45)
for change please input:                    change name tel.   (example: change Denys 2345789)
for reading please input:                   phone name         (example: phone Denys)
--------------------------------------------------------------------------------------------------""")
        except KeyError:
            print("This user was not found in the phone book!")
        except ValueError:
            print("Invalid value. Try again.")
        except TypeError:
            print("Invalid value. Try again.")
        return result
    return wrapper


def welcome_bot(func):
    def inner(*args, **kwargs):
        print("-"*32+"\nWelcome to Assistant Console Bot\n"+"-"*32)
        return func(*args, **kwargs)
    return inner

#add name and number in dict
@error_handler
def attach(name: str, number: str):
    if name in CONTACTS_ARRAY.keys():
        return f'Contact with name {name} already in the phone book'
    CONTACTS_ARRAY[name] = number
    return f'Contact with name {name} and phone {number} add successful'
   
# change number contact
@error_handler
def change(name:str, number:str):
    if name not in COMMAND_ARRAY.keys():
        raise KeyError
    COMMAND_ARRAY[name] = number

def change(*args):
    name = args[0]
    phone = args[1]
    old_phone = CONTACTS_ARRAY.get(name)
    if old_phone:
        CONTACTS_ARRAY[name] = phone
        return f'Phone for contact {name} successful changed'
    return f'In phone book no contact with name {name}'
        

# take phone from dict 
@error_handler
def get_phone(name: str):
    return COMMAND_ARRAY[name]


# ask get phone give phone by name
@error_handler
def show_phone(name: str):
    look_phone = get_phone(name)
    if look_phone: 
        return look_phone
    

# read dict with contact
def reader():
    if not CONTACTS_ARRAY:
        return "Your contact list is empty."
    array_message = ''
    for name, number in CONTACTS_ARRAY.items():
        array_message += ('|{:<12}|{:<15}\n'.format(name, number))
    return array_message

# say good bye and exit
@error_handler
def say_good_bye():
    return "Bye! Bye!"

def no_command(*args):
    return 'Unknown command. Try again'

COMMAND_ARRAY = {
    "hello": lambda: print("May I help you?"),
    "add": attach,
    "change": change,
    "phone": show_phone,
    "show all":reader,
    'exit': say_good_bye,
	'bye': say_good_bye,
	'quit': say_good_bye,
	'close': say_good_bye,
	'.': say_good_bye
}


@error_handler
def parser(command):
    for key in COMMAND_ARRAY.keys():
        if command.startswith(key):
            new_line = command[len(key):].title()
            return COMMAND_ARRAY[key], new_line.split()
    return no_command, []
            


@ welcome_bot
def main():
    while True:
        user_input = input("Please enter your command: ").lower().strip()
        command, data = parser(user_input)
        
        print(command(*data))
        
        if command == say_good_bye:
            break

if __name__ == "__main__":
    main()