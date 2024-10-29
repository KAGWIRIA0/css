#Dictionary
#list[], tuple(), dictionary{}
from tuples import people

student= {"name":"Mary Jane", "id":1234, "age":21, "gender":"F"}

print(student["name"]) #key
print(student)

student["weight"]=61

print(student)


# set --only one existence per item, unordered, mutable
people={"Jane", "Kevoh", "Said","Jane"}
print(people)
people.add( "Alice")
print(people)
print(len(people))
people.discard("Kevoh")
print(people)