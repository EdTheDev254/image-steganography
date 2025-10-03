my_message = "Hello, World!"

binary_message = ''.join(format(ord(char), '08b') for char in my_message)

print(binary_message)
