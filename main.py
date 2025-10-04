#This is the main project codebase for image steganography
import cv2
import pandas as pd

#Convert text to binary
def text_to_bits(message):
    text = "".join(format(ord(c), '08b') for c in message)
    return text 

#we read the image first
image = cv2.imread('copilot-bot.png')

# try if the image is read properly
if image is None:
    raise FileNotFoundError("Image not found. Please check the path.")


# message to be hidden
my_message = "Hello, World!"
# convert message to binary
my_message_bits = text_to_bits(my_message)

# we need to store the length of the message in the first 32 bits for extraction later
# how does this work?
# we get the length of the binary message in bits
# format(value, '032b') converts the integer value to a binary string padded with leading zeros to ensure it is 32 bits long
message_length = len(my_message_bits)
message_length_bits = format(message_length, '032b')

#now we prepend the length of the message to the actual message
my_message_bits = message_length_bits + my_message_bits

# reshaping the image to a 2D array of pixels why?
# because we want to work with each pixel individually 
# and each pixel has 3 values (R,G,B)
# so we reshape the image to a 2D array where each row is a pixel and each column is a color channel
# -1 means we want to infer the number of rows based on the number of columns
# image.shape[-1] is the number of color channels (3 for RGB)
# so the resulting shape will be (number of pixels, 3)
# no need to flatten the image, just reshape it
# because we want to keep the color channels intact for each pixel

pixels = image.reshape(-1, image.shape[-1]) 

#print(my_message_bits)
#print(pixels[:10]) # Print the first 10 pixels to verify the reshaping


