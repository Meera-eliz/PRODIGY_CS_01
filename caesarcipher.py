def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                shifted = (ord(char) - ord('a') + shift) % 26 + ord('a')
            else:
                shifted = (ord(char) - ord('A') + shift) % 26 + ord('A')
            result += chr(shifted)
        else:
            result += char
    return result

def encrypt(text, shift):
    return caesar_cipher(text, shift, 'encrypt')

def decrypt(text, shift):
    return caesar_cipher(text, shift, 'decrypt')

def main():
    choice = input("Enter 'e' to encrypt or 'd' to decrypt: ")
    if choice.lower() == 'e':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice.lower() == 'd':
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_message = decrypt(message, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Please enter 'e' or 'd'.")

if __name__ == "__main__":
    main()
