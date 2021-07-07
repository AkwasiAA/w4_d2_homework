class Task:
    
    def __init__(self, description, user, duration, completed = False,  id = None, ):
        # completed = False with these you are setting up default arguments. These are automatically assigned and dont need to bee entered in your self. You can modify if you want to.
        self.description = description
        self.user = user
        self.duration = duration
        self.completed = completed
        self.id = id
        
    def mark_complete(self):
        self.completed = True