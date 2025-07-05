# def gr():
#     print("HI i heard your strong *u*")
# gr()    

# def add(a,b):  #positional argument
#     return a + b
# result = add(3,5)

# def sub(a,b):
#     return a - b
# result = sub(3,5)

# def mul(a,b):
#     return a * b
# result = mul(3,5)

# def div(a,b):
#     return a / b
# result = div(3,5)

# def solo_leveling(name='Doraemon'):  #Default argument
#     print("Most powerfull character in solo leveling is:",name)
# solo_leveling()
# solo_leveling("Jinwoo")    

# def student(name,age): #keyword argument
#     print(name, "is" ,age ,"years old")
# student(name = "Dj Alok" , age = 28)    

# def square(n):
#     return n*n
# x = int(input("Enter a number to square it: "))
# print("X * X",square(x))

# def get(): #return multiple values
#     return 10,20,30

# a,b,c = get()
# print(a,b,c)

# def show():
#     print("Hello")
# def si():
#     return "Hellb"

# x = show()
# y = si()

# print('x:',x)
# print('y:',y)

#types of fx

#1.built in fx

# print(len('goku'))
# print(max(1,2,3,4,5))
# print(round(8.5))

#2.User defined fx

# def g(name):
#     return 'hello ' + name
# print(g('Goku'))



#3.Lambda fx
#syntax lambda aeguments: expression

# square = lambda x:x * x
# print(square(5))

# add = lambda a,b:a + b
# print(add(45,532))

#map()

# nums = [1,2,3,4]
# squared = list(map(lambda x:x ** 2,nums))
# print(squared)

#filter()

nums = [1,2,3,4,5,6,7]
odd = list(filter(lambda a:a % 2 != 0,nums))
print(odd)