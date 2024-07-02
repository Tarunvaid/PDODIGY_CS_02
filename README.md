# Pixel Manipulation for Image Encryption

## Description

The **Image Encryption Tool** is a Python-based project designed to demonstrate basic image encryption and decryption using pixel manipulation techniques. This tool allows users to encrypt and decrypt images by performing mathematical operations and pixel shuffling. The primary objective is to showcase how simple transformations can be applied to digital images to obscure and later retrieve their content.

### Key Features

- **Encryption and Decryption**: Secure your images by encrypting them with a user-defined key and later decrypting them with the same key.
- **Pixel Manipulation**: Utilize pixel value modifications and pixel shuffling to transform the image data.
- **Lossless Image Processing**: By using the PNG format, ensure that the image quality remains intact during the encryption and decryption processes.
- **Educational Purpose**: Ideal for learning basic concepts of image processing, encryption, and working with Python libraries like Pillow and NumPy.

### Why Use PNG Format?

While JPEG is a common image format, it uses lossy compression, which can degrade image quality every time an image is saved. This project uses PNG format to ensure that image data is preserved exactly as intended, maintaining data integrity which is critical for the encryption and decryption processes.

## Installation

1. **Install Python**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. **Install Required Libraries**: Install the necessary Python libraries using pip.

```sh
pip install pillow numpy
```

## Usage

1. **Place the Image**: Ensure you have an image file (e.g., `input_image.png`) in the project directory or specify the path to the image file.

2. **Run the Script**: Execute the script and follow the prompts to encrypt or decrypt an image.

```sh
python image_encryption.py
```

### Example Usage

When you run the script, you will be prompted to choose whether to encrypt or decrypt an image, provide the input and output image paths, and enter the encryption/decryption key.

```
Do you want to (e)ncrypt or (d)ecrypt an image? e
Enter the path to the input image: input_image.png
Enter the path to the output image (including file name): encrypted_image.png
Enter the encryption/decryption key (integer): 1234
```

### Common Issues and Solutions

1. **ModuleNotFoundError: No module named 'PIL'**
   - Solution: Install the Pillow library using `pip install pillow`.

2. **ModuleNotFoundError: No module named 'numpy'**
   - Solution: Install the numpy library using `pip install numpy`.

3. **FileNotFoundError: [Errno 2] No such file or directory: 'input_image.png'**
   - Solution: Ensure the input image file exists at the specified path.

4. **OverflowError: Python integer out of bounds for uint8**
   - Solution: Convert pixel values to `int32` before performing operations and then back to `uint8` after the operations.

5. **Degraded Image Quality**
   - Solution: Use PNG format instead of JPEG to avoid lossy compression and ensure data integrity.

## Conclusion

This project demonstrates basic image encryption and decryption using pixel manipulation. By using the PNG format, we ensure that the image quality is maintained throughout the process. Feel free to explore and modify the code to enhance the encryption and decryption methods.
```

