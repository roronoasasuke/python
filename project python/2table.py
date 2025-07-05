def table(a,b):
    return a * b
n = int(input("Enter the number of 2 table you want :"))
for b in range(1,n):
 a = 2
#  b = int(input("Enter a number to multiply with 2 X "))
 result = table(a,b)
 print(f"{a} X {b} = {result}")
 