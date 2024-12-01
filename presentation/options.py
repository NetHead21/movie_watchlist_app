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
        succcess, result = (
            self.command.execute(data) if data else self.command.execute()
        )

        if succcess and isinstance(result, str):
            print(self.success_message.format(result=result))

    def __str__(self) -> str:
        return self.name
