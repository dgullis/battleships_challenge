class ToDoList():
    def __init__(self):
        self.tasks = []
    
    def add(self, task):
        self.tasks.append(task)
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object

    def format(self):
        return  self.tasks
        # Returns:
        #   Strings showing the remaining tasks 

    def complete(self, taskNum):
        if taskNum >= len(self.tasks) or taskNum < 0:
            raise Exception("No such task to mark complete")
        self.tasks.remove(self.tasks[taskNum - 1])

        # Parameters:
        #   taskNum: int representing position of task
        # Returns:
        #   Nothing
        # Side-effects:
        #   removes task from the tasks variable