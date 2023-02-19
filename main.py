from choices import add_choice, init_choices

def calculate_age_handler():
    """
    Calculate and prints age data
    """

def quit_app_handler():
    """
    Quit the app
    """

def prepare_choices():
    """
    Sets app choices handlers
    """
    add_choice(label="1", description="Calculate age", handler=calculate_age_handler)
    add_choice(label="q", description="quit the app", handler=quit_app_handler)

def init_app():
    """
    Init App
    (Runs the choices)
    """
    prepare_choices()
    init_choices()

init_app()
