def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def shiftcipher(string, key):
    """Encrypts text using a Caesar cipher.
    """
    key = len(key)
    cipher_text = []
    for i in range(len(string)):
        char = string[i]
        if (char.isupper()):
            cipher_text += chr((ord(char) + key - 65) % 26 + 65)
        else:
            cipher_text += chr((ord(char) + key - 97) % 26 + 97)
    return cipher_text

def viginerecipher(string, key):
    """Encrypts text using a Viginere cipher.
    """
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))

def main():
    text = input("Enter text: ") 
    key = input("Enter key: ")
    key = generateKey(text, key)

    ciphertext = shiftcipher(text, key)
    ciphertext = viginerecipher(ciphertext, key)
    print("Ciphertext :", ciphertext)
    

if __name__ == "__main__":
    main()