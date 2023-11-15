class TaskFormatter:
    def __init__(self, task):
        self.task = task

    def format(self):
        done = "x"
        if self.task.complete == False:
            done = " "
        return (f"[{done}] {self.task.title}")