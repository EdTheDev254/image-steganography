my_message = "Hello, World!"

binary_message = ''

# for i in my_message:
#     binary_message += format(ord(i), '08b')

#Below is a single line statement and does the same thing as above loop
binary_message = ''.join(format(ord(char), '08b') for char in my_message)

print(binary_message)
