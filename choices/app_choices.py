available_choices = []
choice_hander_active = False

def add_choice(label, description, handler):
    available_choices.append((label, description, handler))

def print_choice_options():
    print("Please choose one option")
    for (label,message,handler) in available_choices:
        print(label + ", " + message)

def get_user_choice():
    """
    Prompts for the input 
    """
    return input("Your choice: ")

def handleChoice():
    global choice_hander_active
    print_choice_options()
    user_choice = get_user_choice()

def init_choices():
    global choice_hander_active
    choice_hander_active = True
    while choice_hander_active:
        handleChoice()


