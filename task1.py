#global variables
key = 5

#encryption function that takes
def encrypt_contents(l : list):
    """For encryption, we use ASCII"""
    
def decrypt_contents(l : list):
    """To decrpyt the encrypted contents, we use the key to trace back from ASCII"""

def write_data(data : list, path : str):
    f = open(path)
    f.write(data)
    f.close()

def main():

    txt = input("Enter the text you wish to encrypt: ")
    
    print(txt, "input value")


main()