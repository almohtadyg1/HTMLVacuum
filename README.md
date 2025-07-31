# HTMLVacuum

**HTMLVacuum** is a Python script that scans HTML files in a specified directory and removes:

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

All `.html` files inside the specified directory will be cleaned in-place.

---

## 📁 Project Structure

```
project/
│
├── templates/               # ← Your HTML files go here
│   ├── index.html
│   ├── about.html
│   └── ...
│
└── clean_html.py            # ← The cleaning script
```

---

## 📌 Notes

- The script **modifies files in-place**. Make backups if needed.
- Only **top-level** `.html` files in the directory are processed (no subfolders, yet).

---

## 🧠 Future Improvements

- ✅ Support nested folders  
- ✅ Add dry-run mode  
- ✅ Add command-line support for dynamic paths  
- ✅ Optional file backup before modification  

---

## 👨‍💻 Author

**Mohtady Bellah**  
🌐 [almohtadyg1.pythonanywhere.com](https://almohtadyg1.pythonanywhere.com/)  
🧠 16 y/o | Self-learning programmer  
💻 Python, JS, HTML/CSS, C++

---

## 📄 License

Free to use, modify, or improve—no license restrictions.  
This is an open project to learn and build something useful.

---

Let me know if you want help adding:
- ✅ Command-line support  
- ✅ A CLI tool (`htmlvacuum`) with `argparse`  
- ✅ A badge or GIF demo for GitHub
