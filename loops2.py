#loops
from sqlalchemy.sql.operators import truediv

while True:
    print("Hello,loops")
    break #stop
scores=[90,65,89,34,67,80,56,62,71,58,98,77,69,70,79,46,87,87]

#for each loop
for score in scores:
    if score >=50 and score <=70 and score % 2 == 0:
        print(score)
