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

def generate_hashes(text):
    md5 = hashlib.md5(text.encode()).hexdigest()
    sha1 = hashlib.sha1(text.encode()).hexdigest()
    sha256 = hashlib.sha256(text.encode()).hexdigest()

    with open("hashes.txt", "w") as f:
        f.write(f"Input: {text}\n")
        f.write(f"MD5:     {md5}\n")
        f.write(f"SHA1:    {sha1}\n")
        f.write(f"SHA256:  {sha256}\n")

    print("\n[+] Hashes saved to hashes.txt")
