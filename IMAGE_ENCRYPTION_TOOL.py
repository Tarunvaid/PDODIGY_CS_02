from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    # Open the image
    image = Image.open(input_path)
    pixels = np.array(image, dtype=np.int32)  # Convert to int32 to avoid overflow

    # Apply a basic mathematical operation to each pixel
    encrypted_pixels = (pixels + key) % 256

    # Swap pixels based on key
    np.random.seed(key)
    shuffled_indices = np.random.permutation(encrypted_pixels.size)
    encrypted_pixels = encrypted_pixels.flatten()
    encrypted_pixels = encrypted_pixels[shuffled_indices]
    encrypted_pixels = encrypted_pixels.reshape(pixels.shape)

    # Convert back to uint8
    encrypted_pixels = encrypted_pixels.astype(np.uint8)

    # Save the encrypted image
    encrypted_image = Image.fromarray(encrypted_pixels)
    encrypted_image.save(output_path, format='PNG')

def decrypt_image(input_path, output_path, key):
    # Open the image
    image = Image.open(input_path)
    pixels = np.array(image, dtype=np.int32)  # Convert to int32 to avoid overflow

    # Unshuffle pixels based on key
    np.random.seed(key)
    shuffled_indices = np.random.permutation(pixels.size)
    unshuffled_indices = np.argsort(shuffled_indices)
    pixels = pixels.flatten()
    pixels = pixels[unshuffled_indices]
    pixels = pixels.reshape(image.size[1], image.size[0], -1)

    # Reverse the mathematical operation
    decrypted_pixels = (pixels - key) % 256

    # Convert back to uint8
    decrypted_pixels = decrypted_pixels.astype(np.uint8)

    # Save the decrypted image
    decrypted_image = Image.fromarray(decrypted_pixels)
    decrypted_image.save(output_path, format='PNG')

if __name__ == "__main__":
    action = input("Do you want to (e)ncrypt or (d)ecrypt an image? ").strip().lower()
    input_path = input("Enter the path to the input image: ").strip()
    output_path = input("Enter the path to the output image (including file name): ").strip()
    key = int(input("Enter the encryption/decryption key (integer): ").strip())

    if action == 'e':
        encrypt_image(input_path, output_path, key)
        print(f"Image encrypted and saved to {output_path}")
    elif action == 'd':
        decrypt_image(input_path, output_path, key)
        print(f"Image decrypted and saved to {output_path}")
    else:
        print("Invalid action. Please choose 'e' to encrypt or 'd' to decrypt.")
