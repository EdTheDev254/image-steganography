# from main branch as a single file 
import cv2

# --- Text to Bits --
def text_to_bits(message: str) -> str:
    return ''.join(format(ord(c), '08b') for c in message)

# --- Bits to Text ---
def bits_to_text(bits: str) -> str:
    return ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))

# --- Encode Message ---
def encode_message(image_path: str, message: str, output_path: str = "encoded.png"):
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Image not found: {image_path}")

        message_bits = text_to_bits(message)
        message_length = len(message_bits)
        message_length_bits = format(message_length, '032b')
        all_bits = message_length_bits + message_bits

        pixels = image.reshape(-1, 3)

        if len(all_bits) > len(pixels) * 3:
            raise ValueError("Message too large to fit in this image.")

        for i, bit in enumerate(all_bits):
            pixel_index, channel_index = divmod(i, 3)
            pixels[pixel_index][channel_index] &= 0xFE
            pixels[pixel_index][channel_index] |= int(bit)

        encoded_image = pixels.reshape(image.shape)
        cv2.imwrite(output_path, encoded_image)
        print(f"✅ Message encoded successfully: {output_path}")

    except Exception as e:
        print(f"Error during encoding: {e}")

# --- Decode Message ---
def decode_message(stego_image: str):
    try:
        image = cv2.imread(stego_image)
        if image is None:
            raise FileNotFoundError(f"Could not open {stego_image}")

        pixels = image.reshape(-1, 3).flatten()

        message_length = int(''.join(str(pixels[i] & 1) for i in range(32)), 2)
        message_bits = ''.join(str(pixels[i] & 1) for i in range(32, 32 + message_length))
        message = bits_to_text(message_bits)
        print("✅ Message decoded successfully.")
        return message

    except Exception as e:
        print(f"Error during decoding: {e}")
        return None

# --- Example Usage ---
if __name__ == "__main__":
    mode = input("Enter mode (encode/decode): ").strip().lower()

    if mode == "encode":
        image_path = input("Enter image path: ").strip()
        message = input("Enter message to hide: ").strip()
        output_path = input("Enter output file name (e.g. encoded.png): ").strip()
        encode_message(image_path, message, output_path)

    elif mode == "decode":
        stego_image = input("Enter image to decode: ").strip()
        message = decode_message(stego_image)
        if message:
            print("Hidden message:\n", message)

    else:
        print("Invalid mode. Use 'encode' or 'decode'.")
