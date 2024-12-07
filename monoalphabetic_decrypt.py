def invert_key(key):
    return {v: k for k, v in key.items()}

def monoalphabetic_decrypt(ciphertext, key):
    inverted_key = invert_key(key)
    plaintext = []
    for char in ciphertext.upper():
        if char in inverted_key:
            plaintext.append(inverted_key[char])
        else:
            plaintext.append(char)
    return ''.join(plaintext)

if __name__ == "__main__":
    from monoalphabetic_key import generate_monoalphabetic_key
    from monoalphabetic_encrypt import monoalphabetic_encrypt

    key = generate_monoalphabetic_key()
    plaintext = "From fairest creatures we desire increase, That thereby beauty's rose might never die, But as the riper should by time decease, His tender heir might bear his memory: But thou contracted to thine own bright eyes, Feed'st thy light's flame with self-substantial fuel, Making a famine where abundance lies, Thy self thy foe, to thy sweet self too cruel: Thou that art now the world's fresh ornament, And only herald to the gaudy spring, Within thine own bud buriest thy content, And tender churl mak'st waste in niggarding: Pity the world, or else this glutton be, To eat the world's due, by the grave and thee. When forty winters shall besiege thy brow, And dig deep trenches in thy beauty's field, Thy youth's proud livery so gazed on now, Will be a tattered weed of small worth held: Then being asked, where all thy beauty lies, Where all the treasure of thy lusty days; To say within thine own deep sunken eyes, Were an all-eating shame, and thriftless praise."
    ciphertext = monoalphabetic_encrypt(plaintext, key)
    decrypted_text = monoalphabetic_decrypt(ciphertext, key)

    print("Ciphertext:", ciphertext)
    print("Decrypted Text:", decrypted_text)
    print("Decryption Key:", key)