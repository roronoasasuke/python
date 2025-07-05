# class student:
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll

#     def display(self):
#         print(f'name: {self.name}, roll: {self.roll}')

# s1 = student('ayanokoji kiyotaka',23)
# s2 = student('yuichi katagiri',54)

# s1.display()
# s2.display()
        
class user:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def show_profile(self):
        print(f"Username : {self.username}, email : {self.email}")

u1 = user('hmmm','hmm@email')
u2 = user('kkk','kkk@email')

u1.show_profile()
u2.show_profile()