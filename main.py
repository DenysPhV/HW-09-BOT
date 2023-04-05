import functools

ARRAY = {}

def input_error(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
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
    return wrapper


def welcome_bot(func):
    def inner(*args, **kwargs):
        print("-"*32+"\nWelcome to Assistant Console Bot\n"+"-"*32)
        return func(*args, **kwargs)
    return inner


@input_error
def handler(enter_input):
    if enter_input.lower() == "hello":
        return "May I help you?"
    
    if enter_input.lstrip()[0:3].lower() == "add":
        ARRAY[enter_input.split(" ")[1]] = enter_input.split(" ")[2]

    if "change" in enter_input.lower():
        ARRAY[enter_input.split(" ")[1]] = enter_input.split(" ")[2]

    if "phone" in enter_input.lower():
        return ARRAY[enter_input.split(" ")[1]]
    
    if "show all" in enter_input.lower():
        if ARRAY == {}:
            array_message = "Your contact list is empty."
        else:
            array_message = "Display contact list book:\n"
            for k, v in ARRAY.items():
                array_message += ("|{:<12}| {:<15}\n".format(k, v))
        return array_message
    
    return "Unknown command, please input correct data or command!"


@ welcome_bot
def main():
    while True:
        enter_input = input("Please enter your command: ")
        if enter_input.strip().lower() in [".", "good bye", "close", "exit", "stop"]:
            print("Bye! Bye!")
            break
        else:
            print_me = handler(enter_input)
            if print_me != None:
                print(print_me)
            continue

if __name__ == "__main__":
    main()