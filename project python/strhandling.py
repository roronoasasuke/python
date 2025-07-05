# text =' abCdefg'
# print(text[::-1])
# print(text[:3])
# print(text[1:4])
# print(text.upper())
# print(text.title())
# print(text.strip().lower().title())
# cleaned = text.strip().title()
# print(cleaned)
# print( text.replace('a','z'))
# print( text.find('e'))
# print(text.split('C'))
# print('>'.join(text))
# num = '12345'
# print(num.isdigit())

# word = 'abc123'
# print(word.isdigit())

email = '  hello@python.com  '
cleaned = email.strip().lower().replace('@','at')
print(cleaned)