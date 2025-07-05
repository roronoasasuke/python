def calci(n1,n2,operation):
    if operation == "add":
        return n1 + n2
    elif operation == "sub":
        return n1 - n2 
    elif operation == "mul":
        return n1 * n2 
    elif operation == "div":
        return n1 / n2
    else:
        print("Given operation is not available T-T")
a = int(input('Enter First number:'))         
b = int(input('Enter second number:'))
o = input("Enter your operation:")
print(calci(a,b,o))         