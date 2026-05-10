class Agent:

    def __init__(self, name, role, model):

        self.name = name
        self.role = role
        self.model = model

    def run(self, task):

        return {
            "agent": self.name,
            "task": task,
            "status": "completed"
        }