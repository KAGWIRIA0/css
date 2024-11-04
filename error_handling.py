#Error handling
x= input("Enter First number: ")
y= input("Enter Second number: ")
z= input("Enter Third number: ")

try:
  x_num =int(x)
  y_num =int(y)
  z_num =int(y)
  print(x_num*y_num*z_num)
except:
  print("Enter Valid Number")