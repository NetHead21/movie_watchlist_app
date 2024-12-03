from presentation.views import print_results


class Option:
    def __init__(
        self,
        name: str,
        command: callable,
        prep_call: callable = None,
        success_message: object = "{result}",
    ) -> None:
        self.name = name
        self.command = command
        self.prep_call = prep_call
        self.success_message = success_message

    def choose(self) -> None:
        data = self.prep_call() if self.prep_call else None
        success, result = self.command.execute(data) if data else self.command.execute()

        formatted_result = ""
        if isinstance(result, list):
            print_results(result)
        else:
            formatted_result = result

        if success:
            print(self.success_message.format(result=formatted_result))

    def __str__(self):
        return self.name
