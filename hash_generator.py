# hash_generator.py

import hashlib

def generate_hashes(text):
    print("\n[+] Generating hashes for:", text)
    print("MD5:     ", hashlib.md5(text.encode()).hexdigest())
    print("SHA1:    ", hashlib.sha1(text.encode()).hexdigest())
    print("SHA256:  ", hashlib.sha256(text.encode()).hexdigest())

def main():
    print("=== Hash Generator ===")
    user_input = input("Enter a string to hash: ")
    generate_hashes(user_input)

if __name__ == "__main__":
    main()
