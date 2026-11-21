# My blueprint for tasks
class Task:
    # This function gets the Task started, setting up parameters and attributes
    def __init__(self, title, completed=False):
         # The attributes must be tied to this class with "self"
         self.title = title
         self.completed = completed
         # "self" tells Python which specific task object is being modified
# This internal function allows me to display readable text with print() instead of a raw memory address
    def __str__(self):
        # Make a task complete with an X or incomplete with a -
        status = "[X]" if self.completed else "[-]"
        # Returns completed string value with the title of the string
        return f"{status} {self.title}"
    # This is a class method, not a manager function
    def task_complete(self):
        # If I have multiple Task objects in my list, 'self' points to the exact one I called using .task_complete(), so Python only marks THAT task and not the others.
        self.completed = True
