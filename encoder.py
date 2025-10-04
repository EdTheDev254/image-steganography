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
my_message = """
Steganography is the practice of hiding secret information within a non-secret carrier, such as an image or an audio file. The goal of steganography is to conceal the presence of the hidden information from unauthorized parties.

In the context of image steganography, a hidden message is embedded within an image by modifying the least significant bits (LSBs) of the image's pixel values. By carefully selecting which bits to modify, the steganographic message can be hidden in a way that is difficult to detect.

Steganographic techniques can be used for various purposes, including secure communication, data hiding, and digital watermarking. In secure communication, steganography can be used to send secret messages through seemingly innocuous channels, such as images or audio files. By embedding the message within the carrier, the communication can be made more secure and resistant to traffic analysis.

Data hiding is another use case for steganography. By hiding data within an image or audio file, sensitive information can be protected from unauthorized access. For example, steganography can be used to hide confidential information within an image that is shared publicly.

Digital watermarking is a related concept to steganography that involves embedding a watermark within a digital object, such as an image or audio file. The watermark can be used to verify the authenticity of the object or to track its ownership.

Steganography is a powerful tool for hiding information, but it also has limitations and potential vulnerabilities. The hidden message can be detected and extracted by an attacker if they have sufficient knowledge and tools. Additionally, steganographic techniques can introduce noise and artifacts into the carrier, which can degrade its quality.

Overall, steganography is a fascinating and complex field that has many practical applications in secure communication, data hiding, and digital watermarking. It requires a deep understanding of signal processing, cryptography, and information theory to implement effectively.
"""
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

pixels = image.reshape(-1, image.shape[-1]) # produces a 2D array of pixels that is array of shape (num_pixels, 3)

#print(my_message_bits)
#print(pixels[:10]) # Print the first 10 pixels to verify the reshaping

# hide the message in the LSB of each pixel
# we will iterate over each bit of the message and each pixel

for i, bit in enumerate(my_message_bits):
    pixel_index = i // 3       # Which pixel row
    channel_index = i % 3      # Which channel (0=R, 1=G, 2=B)
    
    # Clear LSB and set it to message bit
    pixels[pixel_index][channel_index] &= 0xFE  # 0xFE = 254 this is the opposite of the message bit
    pixels[pixel_index][channel_index] |= int(bit) # this is the message bit that we want to hide


# use enumerate and list comprehension to achieve the same result as above loop
# for i, bit in enumerate(my_message_bits):
# single line version of the above loop
#     pixel = list(pixels[i])
#     pixel[0] = (pixel[0] & ~1) | int(bit)
#     pixels[i] = tuple(pixel)


print(pixels[:20]) # Print the first 10 pixels to verify the LSB modification

# reshape the modified pixels back into the original image dimensions
image_modified = pixels.reshape(image.shape)

# save the modified image
cv2.imwrite('copilot-bot-modified.png', image_modified)

