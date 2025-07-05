age = int(input("Enter YOur Age : "))
if age > 0:
  if age<12:
    print("you have to pay 5 rupees")
  elif age >= 12 and age <= 20:
    print("you have to pay 10 rupees")
  elif age > 20 and age <= 40:
    print("you have to pay 20 rupees")
  else:
    print("NO need to pay ^v^")
else:
  print("how can your Age can be minus LOL")