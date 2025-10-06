import cv2

def extract_message(stego_image):
    try:
        # Load the image
        image = cv2.imread(stego_image)

        if image is None:
            raise FileNotFoundError(f"Could not open {stego_image}")

        # Flatten the image into a 1D array
        pixels = image.reshape(-1, 3).flatten()

        # Extract the message length (32 bits)
        message_length = int(''.join(format(pixels[i] & 1, '01b') for i in range(32)), 2)

        # Extract the message bits
        message_bits = [format(pixels[i] & 1, '01b') for i in range(32, 32 + message_length)]

        # Convert the bits to text
        message = ''.join(chr(int(''.join(message_bits[i:i+8]), 2)) for i in range(0, len(message_bits), 8))

        return message

    except FileNotFoundError:
        print(f"File not found: {stego_image}")
        return None

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Call the function with the stego image
message = extract_message('copilot-bot-modified.png')

if message is not None:
    # Save the message to a file if desired
    with open('extracted_message.txt', 'w') as f:
        f.write(message)

    print(f"Message extracted: {message}")
else:
    print("Error extracting message.")