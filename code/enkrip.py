# Generate vector untuk kunci
keyMatrix = [[0] * 3 for i in range(3)]
# Generate vector untuk plain text
textVector = [[0] for i in range(3)]
# Generate vector untuk cipher text
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
    """Enkripsi dengan Caesar Cipher
    """
    key = len(key)
    cipher_text = []
    for i in range(len(string)):
        char = string[i]
        if (char.isupper()):  # UNICODE
            cipher_text += chr((ord(char) + key - 65) % 26 + 65)
        else:
            cipher_text += chr((ord(char) + key - 97) % 26 + 97)
    return cipher_text


def vigenerecipher(string, key):
    """Enkripsi dengan Vigenere Chiper
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

# Fungsi untuk mengenkripsi kan text
def encrypt(textVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] *
                                       textVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26


def HillCipher(message, key):

    # Mendapatkan matrix kunci dari string kunci
    getKeyMatrix(key)

    # Generate vector untuk plain text
    for i in range(3):
        textVector[i][0] = ord(message[i]) % 65

    # Memanggil fungsi untuk mengenkripsi
    encrypt(textVector)

    # Generate text yang sudah di enkripsi dari vector
    CipherText = []
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))

    # Return hasil cipher text
    return "".join(CipherText)


def main():
    text = raw_input("Enter text: ")
    key = raw_input("Enter key: ")
    key = generateKey(text, key)
    ciphertext = shiftcipher(text, key)
    ciphertext = vigenerecipher(ciphertext, key)
    ciphertext_list = [ciphertext[i:i+3] for i in range(0, len(text), 3)]
    hasil = ''
    for i in ciphertext_list:
        if len(i) < 3:
            i = i + "X" * (3 - len(i))
        hasil += HillCipher(i, key)

    print("Ciphertext: ", hasil)
    # print("Ciphertext :", ciphertext)


if __name__ == "__main__":
    main()
