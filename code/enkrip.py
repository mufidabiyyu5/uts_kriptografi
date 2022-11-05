# Generate vector for the key
keyMatrix = [[0] * 3 for i in range(3)]
# Generate vector for the message
messageVector = [[0] for i in range(3)]
# Generate vector for the cipher
cipherMatrix = [[0] for i in range(3)]

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
        if (char.isupper()):##UNICODE 
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

def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
 
# Following function encrypts the message
def encrypt(messageVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] *
                                       messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26
 
def HillCipher(message, key):
 
    # Get key matrix from the key string
    getKeyMatrix(key)
 
    # Generate vector for the message
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65
 
    # Following function generates
    # the encrypted vector
    encrypt(messageVector)
 
    # Generate the encrypted text
    # from the encrypted vector
    CipherText = []
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))
 
    # Finally print the ciphertext
    # print("Ciphertext: ", "".join(CipherText))
    return "".join(CipherText)

def main():
    text = input("Enter text: ") 
    key = input("Enter key: ")
    key = generateKey(text, key)
    ciphertext = shiftcipher(text, key)
    ciphertext = viginerecipher(ciphertext, key)
    ciphertext_list = [text[i:i+3] for i in range(0, len(text), 3)]
    hasil = ''
    for i in ciphertext_list:
        if len(i) < 3:
            i = i + "X" * (3 - len(i))
        hasil += HillCipher(i, key)
    
    print("Ciphertext: ", hasil)
    # print("Ciphertext :", ciphertext)
    

if __name__ == "__main__":
    main()