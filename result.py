import json


class Result():
    def __init__(self):
        self.data = None
        self.errors = None
        self.succeed = None

    @staticmethod
    def success(model):
        result = Result()
        result.data = model
        result.succeed = True
        result.errors = None
        return result

    @staticmethod
    def fail(error, data = None):
        result = Result()
        result.data = data
        result.succeed = False
        if error:
            result.errors = error.__dict__
        return result

    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def apiResult(self):
        return self.json(), 200, {'Content-Type': 'text/json; charset=utf-8'}
  
    

