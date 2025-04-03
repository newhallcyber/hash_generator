# hash_generator.py

import hashlib
import pyperclip

def generate_hashes(text):
    hashes = {
        "MD5": hashlib.md5(text.encode()).hexdigest(),
        "SHA1": hashlib.sha1(text.encode()).hexdigest(),
        "SHA256": hashlib.sha256(text.encode()).hexdigest()
    }

    with open("hashes.txt", "w") as f:
        f.write(f"Input: {text}\n")
        for algo, value in hashes.items():
            print(f"{algo}: {value}")
            f.write(f"{algo}: {value}\n")

    return hashes

def copy_to_clipboard(hashes):
    print("\nWhich hash would you like to copy?")
    for i, algo in enumerate(hashes.keys(), 1):
        print(f"{i}. {algo}")
    choice = input("Enter the number (or press Enter to skip): ")

    if choice in ["1", "2", "3"]:
        algo = list(hashes.keys())[int(choice) - 1]
        pyperclip.copy(hashes[algo])
        print(f"[+] {algo} hash copied to clipboard.")
    else:
        print("[-] No hash copied.")

def main():
    print("=== Hash Generator ===")
    user_input = input("Enter a string to hash: ")
    hashes = generate_hashes(user_input)
    copy_to_clipboard(hashes)

if __name__ == "__main__":
    main()
