# functions
import math
from datetime import date




def calc_area_triangle(b,h):
    area= 0.5 * (b*h)
    print(area)

def cal_area_circle(radius):
    area = 22/7 * radius*radius
    area= round(area, 2)
    print("Area of circle is",area,"cm^2")

def print_todays_date():
    today= date.today()
    print(today)

def add(*arge):
    total=0
    for num in arge:
     total +=num
    print("Total is",total)

def sayHi(name,age=21):
    print("Hello ",name,"I am",age,"years old")

sayHi("Faith,")
sayHi("Neema,".upper(),23)


# users=["A","B","C"]
#users.sort(reverse=true)


#use a func ==calling
calc_area_triangle(10,20)
calc_area_triangle(12,40)

triangles= [[8,9],[5,6],[4,7],[24,10],[8.5,6.6]]

for t in triangles:
    calc_area_triangle(t[0],t[1])


cal_area_circle(10)
cal_area_circle(28.73653)

print_todays_date()

add(1,2)
add(7,8,9)
add(122,267,90,43)



