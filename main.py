import functools
CONTACTS_ARRAY = {}

def error_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = False

        try:
            result = func(*args, **kwargs)
        except IndexError:
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
        return result
    return wrapper


def welcome_bot(func):
    def inner(*args, **kwargs):
        print("-"*32+"\nWelcome to Assistant Console Bot\n"+"-"*32)
        return func(*args, **kwargs)
    return inner

@error_handler
def attach(name: str, number: str):
    if name in CONTACTS_ARRAY.keys():
        return "Unknown command, please input correct data or command!"
    CONTACTS_ARRAY[name] = number   
   
   
def change():
    ...

def show_phone():
    ...

def reader():
    array_message = "Your contact list is empty."
    for name, number in CONTACTS_ARRAY.items():
        array_message += ('|{:<12}|{:<15}\n'.format(name, number))
    return array_message

@error_handler
def say_good_bye():
    print("Bye! Bye!")
    exit()

COMMAND_ARRAY = {
    "hello": lambda: print("May I help you?"),
    "add": attach,
    "change": change,
    "phone": show_phone,
    "show all": lambda: print(reader()),
    'exit': say_good_bye,
	'bye': say_good_bye,
	'quit': say_good_bye,
	'close': say_good_bye,
	'.': say_good_bye
}


def parser(command):
    for key in COMMAND_ARRAY.keys():
        if command.startswith(key):
            new_line = command[len(key):].title()
            COMMAND_ARRAY[key](*new_line.split())
            break




@ welcome_bot
def main():
    while True:
        command = input("Please enter your command: ").lower().strip()
        parser(command)

if __name__ == "__main__":
    main()