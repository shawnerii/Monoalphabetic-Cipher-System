from monoalphabetic_key import generate_monoalphabetic_key
from monoalphabetic_encrypt import monoalphabetic_encrypt
from monoalphabetic_decrypt import monoalphabetic_decrypt
from monoalphabetic_analysis import frequency_analysis_attack

def main():
    key = generate_monoalphabetic_key()
    print("Generated Key:", key)
    
    plaintext = "From fairest creatures we desire increase, That thereby beauty's rose might never die, But as the riper should by time decease, His tender heir might bear his memory: But thou contracted to thine own bright eyes, Feed'st thy light's flame with self-substantial fuel, Making a famine where abundance lies, Thy self thy foe, to thy sweet self too cruel: Thou that art now the world's fresh ornament, And only herald to the gaudy spring, Within thine own bud buriest thy content, And tender churl mak'st waste in niggarding: Pity the world, or else this glutton be, To eat the world's due, by the grave and thee. When forty winters shall besiege thy brow, And dig deep trenches in thy beauty's field, Thy youth's proud livery so gazed on now, Will be a tattered weed of small worth held: Then being asked, where all thy beauty lies, Where all the treasure of thy lusty days; To say within thine own deep sunken eyes, Were an all-eating shame, and thriftless praise."
    ciphertext = monoalphabetic_encrypt(plaintext, key)
    print("\nCiphertext:", ciphertext)
    
    decrypted_text = monoalphabetic_decrypt(ciphertext, key)
    print("\nDecrypted Text:", decrypted_text)

    print("\nAttempting Brute-Force Attack:")
    bruteforce_decrypted_text = frequency_analysis_attack(ciphertext)
    print("Brute-Force Decrypted Text:", bruteforce_decrypted_text)

if __name__ == "__main__":
    main()