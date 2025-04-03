import hashlib
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_hashes():
    text = entry.get()
    if not text:
        messagebox.showwarning("Input Error", "Please enter a string.")
        return

    md5_hash = hashlib.md5(text.encode()).hexdigest()
    sha1_hash = hashlib.sha1(text.encode()).hexdigest()
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()

    md5_var.set(md5_hash)
    sha1_var.set(sha1_hash)
    sha256_var.set(sha256_hash)

    with open("hashes.txt", "w") as f:
        f.write(f"Input: {text}\n")
        f.write(f"MD5: {md5_hash}\n")
        f.write(f"SHA1: {sha1_hash}\n")
        f.write(f"SHA256: {sha256_hash}\n")

def copy_hash(value):
    pyperclip.copy(value)
    messagebox.showinfo("Copied", "Hash copied to clipboard!")

# Set up GUI
root = tk.Tk()
root.title("Hash Generator")
root.geometry("600x300")
root.resizable(False, False)

tk.Label(root, text="Enter Text:", font=('Arial', 12)).pack(pady=10)
entry = tk.Entry(root, width=60)
entry.pack()

tk.Button(root, text="Generate Hashes", command=generate_hashes, bg="#4CAF50", fg="white").pack(pady=10)

# Display Hashes
md5_var = tk.StringVar()
sha1_var = tk.StringVar()
sha256_var = tk.StringVar()

for algo, var in [("MD5", md5_var), ("SHA1", sha1_var), ("SHA256", sha256_var)]:
    frame = tk.Frame(root)
    frame.pack(pady=2)
    tk.Label(frame, text=f"{algo}:", width=8).pack(side=tk.LEFT)
    tk.Entry(frame, textvariable=var, width=60).pack(side=tk.LEFT)
    tk.Button(frame, text="Copy", command=lambda v=var: copy_hash(v.get())).pack(side=tk.LEFT)

root.mainloop()
