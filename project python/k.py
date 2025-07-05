# for name in range(5) :   
#   name = "ram"
#   age = 80
#   print(f"My name is {name} and my age is {age}")
# name = "ani"
# age = 18
# height = 6.2
# is_student = False
# skills = ["py","c","java"]
# print(f"name :{name}\nage : {age}\nheight :{height}\nskills :{skills}")  
# print(type(name))
# print(type(age))
# a = 1000
# b = 7
# print(f"addition :{a+b}")
# print(f"subtraction :{a-b}")
# print(f"multiplication :{a*b}")
# print(f"division :{a/b}")
# print(f"power :{a**b}")
# print(f"quotient :{a//b}")
# print(f"remainder :{a%b}")
my_csh = int(input("Enter your cash :"))
student = int(input("Enter number of students : "))
chcl_price = int(input("Enter Price of one chocolate : ")) 
total = my_csh//chcl_price
change =  my_csh%chcl_price
if total > student:
 print(f"Total chocolates i can buy is {total} change {change} ")
 print(f"if chocolates get distributed among {student} students, remaining {total-student} chocolates i wiil take")
else:
 print(f"Total chocolates {total} are kept by me" )