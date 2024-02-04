import json


class ErrorResult():
    def __init__(self, message) -> None:
        self.message = message
    def json(self):
        return json.dumps(self.__dict__)
