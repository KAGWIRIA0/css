#inheritance
#error handling
#dates
from datetime import datetime,date


class Employee:
    def __init__(self, name, id_number, dob, gender):
        self.name = name
        self.id_number = id_number
        self.dob = dob
        self.gender = gender
        date_of_birth = datetime.strptime(dob, "%Y-%m-%d") #01-01-2024
        self.age= date.today().year-date_of_birth.year

    def print_details(self ):
        print(f"Name: {self.name}\n ID: {self.id_number}\nDOB: {self.dob}\nGender: {self.gender}")

class PermanentEmployee(Employee):
          def __init__(self, name,id_number, dob, gender, salary):
              super().__init__(name,id_number,dob,gender)
              self.salary = salary

          def print_salary(self):
              print(f"Salary is: {self.salary}")
             #override
          def print_details(self):
                super().print_details()
                print(f"Salary is: {self.salary}")

class TemporaryEmployee(Employee):
          def __init__(self, name,id_number, dob, gender, hourly_pay,end_date):
              super().__init__(name,id_number,dob,gender)
              self.hourly_pay = hourly_pay
              self.end_date = end_date

          def print_hourly_pay(self):
              print(f"Hourly payment is: {self.hourly_pay}")

          def print_end_date(self):
              print(f"End date is: {self.end_date}")

p1= PermanentEmployee(salary=32000, name="Jessica Williams",id_number="23478658", gender="F",dob="1991-01-21")
p1.print_details()
p1.print_salary()

t1=TemporaryEmployee("Hailey","22901254","1993-10-22","M",3000,"2024-12-31")
t1.print_details()