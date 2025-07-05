# print(10/0) #zerodivision error
# int('abc') #VAlueerror
# open('idk.txt') #file not found error

# try:
#     print(10/2)
# except ZeroDivisionError:
#     print('how the F can u divide with zero BAKA!')
# finally:
#     print('NIce ^V^')
# try:
#     num = int(input('type any number ok-->'))
# except ValueError:
#     print('i said to type numbers T-T')
# finally:
#     print('correct')     

# try:
#     num = int(input('enter number-->'))
#     result = 10 / num
# except ValueError:
#     print('only numbers')
# finally:
#     print('close') 

try:
    f = open('fx.txt','r')
    data = f.read()

finally:
    print('close the program')        