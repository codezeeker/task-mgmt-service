from json import JSONEncoder

class Task:
    id = int
    task = str
    completed = bool
    def __init__(self, id, task, completed):
        self.id = id
        self.task = task
        self.completed = completed

# subclass JSONEncoder
class EmployeeEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__