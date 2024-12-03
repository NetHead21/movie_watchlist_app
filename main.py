from presentation import get_option_choice
from presentation.menu import options
from presentation.views import print_options


def loop() -> None:
    print_options(options)
    chosen_option = get_option_choice(options)
    chosen_option.choose()

    _ = input("Please Enter to return to menu.")


if __name__ == "__main__":
    while True:
        loop()
