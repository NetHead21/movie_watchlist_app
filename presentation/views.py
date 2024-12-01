from presentation import clear_screen


def print_line() -> None:
    print("=" * 30)


def print_options(options: dict) -> None:
    clear_screen()
    print_line()
    for shortcut, option in options.items():
        print(f"{shortcut}: {option}")
    print()
