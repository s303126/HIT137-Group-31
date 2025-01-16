import string
import easygui as es

def encrypt_text(file_path, output_path, n, m):
    """
    Encrypts the content of a file using a custom substitution cipher and writes the encrypted content to another file.

    Parameters:
        file_path (str): Path to the input file.
        output_path (str): Path to save the encrypted file.
        n (int): First key parameter for the cipher.
        m (int): Second key parameter for the cipher.
    """
    with open(file_path, 'r') as file:
        raw_text = file.read()

    encrypted_text = ""
    for char in raw_text:
        if char in string.ascii_lowercase:
            shift = (n * m) if char <= 'm' else (n + m)
            encrypted_text += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        elif char in string.ascii_uppercase:
            shift = n if char <= 'M' else m**2
            encrypted_text += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_text += char

    with open(output_path, 'w') as file:
        file.write(encrypted_text)

def decrypt_text(file_path, n, m):
    """
    Decrypts the content of a file that was encrypted with the custom cipher.

    Parameters:
        file_path (str): Path to the encrypted file.
        n (int): First key parameter for the cipher.
        m (int): Second key parameter for the cipher.

    Returns:
        str: The decrypted text.
    """
    with open(file_path, 'r') as file:
        encrypted_text = file.read()

    decrypted_text = ""
    for char in encrypted_text:
        if char in string.ascii_lowercase:
            shift = (n * m) if ((ord(char) - ord('a')) - (n * m)) % 26 <= 12 else (n + m)
            decrypted_text += chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
        elif char in string.ascii_uppercase:
            shift = n if ((ord(char) - ord('A')) - n) % 26 <= 12 else m**2
            decrypted_text += chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        else:
            decrypted_text += char

    return decrypted_text



def verify_decryption(original_file_path, decrypted_text):
    with open(original_file_path, 'r') as file:
        original_text = file.read()

    return original_text == decrypted_text

# Select what to do (encrypt vs decrypt)
choice = es.buttonbox("what do you want to do", choices = ["Encrypt", "Decrypt"])

if choice == "Encrypt":
    
    to_encrypt = es.fileopenbox("Select the file to encrypt")
    output = es.filesavebox("Select where to store encrypted file",default="encrypted_text.txt")
    
    # Encrypt the file
    encrypt_text(to_encrypt, output, 2, 3)
    
elif choice == "Decrypt":
    
    to_decrypt = es.fileopenbox("Select the file to decrypt")
    
    # Decrypt the file
    decrypted_text = decrypt_text(to_decrypt, 2, 3)
    
    # Verify the correctness of decryption
    to_check = es.fileopenbox("Select the check file")
    is_correct = verify_decryption(to_check, decrypted_text)
    print("Decryption is correct!" if is_correct else "Decryption failed.")
    
else:
    es.msgbox("Exiting...")



