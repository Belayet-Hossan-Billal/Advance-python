class Person:
    name = ""
    age = 0
    def __int__(self, personName, personAge):
        self.name = personName
        self.age = personAge
    def showName(self):
        print(self.name)
    def showage(self):
        print(self.age)