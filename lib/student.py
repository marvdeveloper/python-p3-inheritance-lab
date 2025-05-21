from lib.user import User  # use absolute import

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, string):
        self.knowledge.append(string)
