# count = int(input("Enter number of counts: "))
# till = int(input("Enter number of times: "))
# while count <= till:
#   print("Count:",count)
#   count += 1
# for i in range(3,9):
#   print("this is line",i) 

# Animes = ["Goku","Vegeta","Saitama","Zeno"]
# for Anime in Animes:
#     print("My Favourite animes",Anime)

# for i in range(3,100):
#     if i == 19:
#         break
#     print(i)

# for i in range(1,6):
#     if i == 3:
#         continue
#     print(i)

# for i in range(3):
#     pass # do nothing for now

# secret = 9
# guess = int(input("GUess a number in 1 to 10 : "))
# if guess < 10:
#   if secret == guess:
#     print("Yea Boy u guessed it rihgt ^v^")
#   elif secret > guess:
#     print("Too low try again")
#   else:
#     print("Too high try again")
# else:
#   print("Giving value out of the box T-T") 
  
secret = 123
for i in range(3):
 guess = int(input("Enter your password : "))
 if secret == guess:
  print("Welcome ^v^")
 else:
  print("Wrong Password try again")

