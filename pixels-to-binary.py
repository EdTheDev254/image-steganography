import cv2
import pandas as pd

image = cv2.imread('copilot-bot.png')
num_pixels = 10
#flatten image to 3D array

pixels = image.reshape(-1, image.shape[-1]) 


#save to csv
df = pd.DataFrame(pixels[:num_pixels], columns=['Blue', 'Green', 'Red'])

# Convert to binary
# def f(x):
#     return format(x, '08b')


# Take each pixel value (0–255).
# Convert it to an 8-bit binary string.
# Return a dataframe (binary_df) where all numbers are now 8-bit binary strings.
binary_df = df.map(lambda x: format(x, '08b'))

# Save the binary values to a CSV file
binary_df.to_csv('pixels.csv', index=False)




