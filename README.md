
# 🔐 CyberHash Generator (Python + Tkinter)

A simple and interactive GUI application that takes user input and returns the MD5, SHA1, and SHA256 hashes of the string. Includes copy-to-clipboard functionality and saves the output to a text file.

---

## 💡 Features

- Easy-to-use graphical interface (built with Tkinter)
- Generates MD5, SHA1, and SHA256 hashes
- Saves hash output to a file (`hashes.txt`)
- Click-to-copy each hash to clipboard (uses `pyperclip`)

---

## 🚀 How to Use

### 1. Clone or Download This Repository

```bash
git clone https://github.com/newhallcyber/cyberhash-generator.git
cd cyberhash-generator
```

### 2. Install Requirements

This app only needs one external package: `pyperclip`.

#### On macOS/Linux:
```bash
pip3 install pyperclip
```

#### On Windows:
Make sure you're installing it to the correct Python version. Use:

```bash
python -m pip install pyperclip
```

You can verify it's working with:

```bash
python -c "import pyperclip; print('pyperclip is working')"
```

---

### 3. Run the App

```bash
python cyberhash_generator.py
```

A window will pop up. Type a string, click "Generate Hashes", and you'll see all three hashes displayed with "Copy" buttons.

---

## 📦 Requirements

- Python 3.x
- `pyperclip` (for clipboard support)
- Tkinter (comes preinstalled with Python on most systems)

---

## 📝 Notes for Windows Users

If `pyperclip` isn’t working:
- Run `where python` and `where pip` to check if they’re aligned
- Use `python -m pip install pyperclip` to be sure you’re installing to the correct version

---

## 📁 Example Screenshot

![image](https://github.com/user-attachments/assets/d5380fc7-0756-4652-ba2a-f45b3ebacdc8)


---

## 🛠️ Future Features

- File hash support
- Dark mode or custom themes
- Hash comparison/check tool

---

## 👨‍💻 Author

Created by Newhallcyber
GitHub: [github.com/newhallcyber](https://github.com/newhallcyber)  
LinkedIn: [linkedin.com/in/stevenellsworthnewhall](https://www.linkedin.com/in/stevenellsworthnewhall/)

---

## ⚠️ Disclaimer

This tool is for educational purposes only.
