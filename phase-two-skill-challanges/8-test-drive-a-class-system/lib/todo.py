class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        if type(task) is not str:
            raise Exception("Todo class only accepts strings as argument!")
        self.task = task
        self.complete = False

    def mark_complete(self):
        self.complete = True