from Affine_Cipher import AffineCipher
from Caesar_Cipher import CaesarCipher

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
    print('"' + message + '"' + " ->", new_cipher, "-> " + new_ciphertext)
    print('"' + new_plaintext + '"' + " <-", new_cipher, "<- " + new_ciphertext)



    cipher2 = CaesarCipher(11)
    ciphertext2 = cipher2.encrypt(message)
    plaintext2 = cipher2.decrypt(ciphertext2)
    print('"' + message + '"' + " ->", cipher2, "-> " + ciphertext2)
    print('"' + plaintext2 + '"' + " <-", cipher2, "<- " + ciphertext2)

    new_cipher2 = CaesarCipher(23)
    new_ciphertext2 = new_cipher2.encrypt(message)
    new_plaintext2 = new_cipher2.decrypt(new_ciphertext2)
    print('"' + message + '"' + " ->", new_cipher2, "-> " + new_ciphertext2)
    print('"' + new_plaintext2 + '"' + " <-", new_cipher2, "<- " + new_ciphertext2)
