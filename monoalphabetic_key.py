import random
import string

def generate_monoalphabetic_key():
    letters = list(string.ascii_uppercase)
    shuffled_letters = letters[:]
    random.shuffle(shuffled_letters)
    return dict(zip(letters, shuffled_letters))

if __name__ == "__main__":
    key = generate_monoalphabetic_key()
    print("Generated Key:")
    for k, v in key.items():
        print(f"{k} -> {v}")