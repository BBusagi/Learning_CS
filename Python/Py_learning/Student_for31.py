class Student:

    def __init__(self, name, major, GPA) :
        self.name = name
        self.major = major
        self.GPA = GPA

    def on_honor_roll(self):
        if self.GPA >= 3.5:
            return True
        else :
            return False
