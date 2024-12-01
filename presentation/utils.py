import os


def clear_screen() -> None:
    clear = "cls" if os.name == "nt" else "clear"
    os.system(clear)


def option_choice_is_valid(choice: str, options: dict) -> bool:
    return choice in options


def format_date(date: str) -> tuple[int, ...]:
    month, day, year = map(int, date.split("/"))
    return year, month, day
