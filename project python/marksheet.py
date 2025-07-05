Name = "suresh"
age = 21
math = 90
art = 90
science = 30
total_marks = math + art + science
average = total_marks/3
print(f"name       :{Name}")
print(f"Total marks:{total_marks}")
print(f"average    :{average}")
print(f"My name is {Name} , I scored {total_marks} out of 300,My Average is {average} ")
if total_marks >= 290:
    print("Grade : O")
elif total_marks >= 260:
    print("Grade : A+")
elif total_marks >= 240:
    print("Grade : A")
elif total_marks >= 210:
    print("Grade : B+")
elif total_marks >= 180:
    print("Grade : B")
else:
    print("Grade : F")