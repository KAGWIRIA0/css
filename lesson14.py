class criminal:
    def __init__(self, name, age, id_number, gender,crime):
        self.name = name
        self.age = age
        self.id_number = id_number
        self.gender = gender
        self.crime= crime
    def show_details(self):
        print(f"Name:{self.name}\nAge:{self.age}\nGender:{self.gender}\nID:{self.id_number}\nIssue: {self.crime}")


 # store data and manipulate data
c1 = criminal("Kyle Walker","33","2546798","Male","Robbery with Violence")
c1.show_details()