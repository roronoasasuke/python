# file = open('abtr.txt','r')
# content = file.read()
# print(content.strip().lower().title())
# file.close()

# file = open('abtr.txt','a')
# file.write('my friend Sriram like to do cosplay')
# file.close

# file = open('abtr.txt','r')
# for line in file:
#     print(line.strip())
# file.close()

# with open('abtr.txt','r') as f:
#   for line in f:
#     print(line.strip())

data = input('enter something that i have to do anything -->')
with open('abtr.txt','w') as f:
    f.write(data)