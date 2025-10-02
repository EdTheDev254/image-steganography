# image-steganography
Hiding information in an image. By using the LSB(Least Significant Bit) of each pixel RGB data, it is possible to
hide a long form of text.
Each pixel in a standard RGB image contains 3 bytes of data (Red, Green, and Blue channels). By modifying only the last bit (LSB) of each channel, it is possible to embed hidden information without noticeably changing the image visually.

- Encode text messages into an image by converting the text into binary and storing the bits inside the pixel data.
- Decode and retrieve the hidden message by reading back the LSBs in the same order.
- Use lossless formats like PNG or BMP (since JPEG compression destroys exact LSB values).

This principle is the same as the Audio LSB project I created:

### How it works
1. Convert the text into a binary string (8 bits per character).
2. Flatten the image pixel data so each channel (R, G, B) can be accessed.
3. Replace the least significant bit of each channel with the message bits.
4. Reshape the modified pixels back into the original image dimensions and save.
