from random import choice

from presentation import option_choice_is_valid


def get_user_input(label: str, required: bool = True) -> str:
    value = input(f"{label}: ") or None
    while required and not value:
        value = input(f"{label}: ") or None
    return value


def get_option_choice(options: dict) -> callable:
    choice = input("Choose an option: ").upper()
    while not option_choice_is_valid(choice, options):
        print("Invalid option. Please try again.")
        choice = input("Choose an option: ").upper()
    return options[choice]
