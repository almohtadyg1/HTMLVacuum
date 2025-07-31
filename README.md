# HTMLVacuum

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Project-Stable-brightgreen)
![License](https://img.shields.io/badge/License-Unlicensed-lightgrey)
![HTML Cleaner](https://img.shields.io/badge/Tool-HTMLVacuum-ff69b4)

**HTMLVacuum** is a Python script that scans HTML files in a specified directory — **including all subfolders** — and removes:

- HTML comments (`<!-- ... -->`)
- JavaScript comments (`// single-line`, `/* multi-line */`)
- CSS comments (`/* multi-line */`)

Perfect for cleaning up source files for production or minimizing clutter in templates.

---

## 🔧 How It Works

The script uses Python’s built-in `html.parser.HTMLParser` to parse and remove comments from:

- The HTML structure
- `<script>` blocks (JavaScript)
- `<style>` blocks (CSS)

It carefully avoids stripping anything inside strings or breaking syntax.

---

## 📂 Directory Configuration

Before running the script, set your target directory at the top of the Python file:

```python
DIR_PATH = "<Put-The-Dir-Path-Here>"  # ← Replace this with your directory path
```

**Example:**

```python
DIR_PATH = "./templates"
```

---

## 🚀 Usage

### 1. Save the Script

Save the file as `clean_html.py`.

### 2. Run It

```bash
python clean_html.py
```

All `.html` files inside the specified directory — including files in all nested subfolders — will be cleaned in-place.

---

## 📁 Project Structure Example

```
project/
│
├── templates/
│   ├── index.html
│   ├── about.html
│   └── blog/
│       └── post.html
│
└── clean_html.py
```

✅ All of the above `.html` files will be processed.

---

## 📌 Notes

- The script **modifies files in-place**. Make backups if needed.
- Processes **all `.html` files recursively**, including deep subdirectories.
- Skips anything that isn’t a `.html` file.

---

## 🧠 Features & Future Improvements

- ✅ Removes all HTML, JS, and CSS comments
- ✅ Recursively supports nested folders  
- 🔄 Optional dry-run mode (coming soon)  
- 🔄 Optional command-line arguments  
- 🔄 Optional file backups before modifying  

---

## 👨‍💻 Author

**Mohtady Bellah**  
🌐 [almohtadyg1.pythonanywhere.com](https://almohtadyg1.pythonanywhere.com/)  
🧠 16 y/o | Self-learning programmer  
💻 Python, JS, HTML/CSS, C++

---

## 📄 License

Free to use, modify, or improve — no license restrictions.  
This is an open project to learn and build something useful.

---

Let me know if you'd like:
- A GIF demo  
- A CLI tool wrapper (`htmlvacuum`)  
- Command-line argument support  
- Backup mode or dry-run feature
