from Affine_Cipher import AffineCipher

if __name__ == '__main__':
    cipher = AffineCipher(5, 5)
    message = "Super secretive message"
    ciphertext = cipher.encrypt(message)
    plaintext = cipher.decrypt(ciphertext)
    print('"' + message + '"' + " ->", cipher, "-> " + ciphertext)
    print('"' + plaintext + '"' + " <-", cipher, "<- " + ciphertext)

    new_cipher = AffineCipher(7, 7)
    new_ciphertext = new_cipher.encrypt(message)
    new_plaintext = new_cipher.decrypt(new_ciphertext)
    print('"' + message + '"' + " ->", cipher, "-> " + ciphertext)
    print('"' + plaintext + '"' + " <-", cipher, "<- " + ciphertext)
