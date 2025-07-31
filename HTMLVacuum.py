import os
import re
from html.parser import HTMLParser

# === Global Directory Path Variable ===
DIR_PATH = "templates"

class CommentStrippingHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.output = []
        self.in_script = False
        self.in_style = False
        self.script_content = ''
        self.style_content = ''

    def handle_decl(self, decl):
        self.output.append(f'<!{decl}>')

    def handle_starttag(self, tag, attrs):
        self.output.append(self.get_starttag_text())
        if tag == 'script':
            self.in_script = True
            self.script_content = ''
        elif tag == 'style':
            self.in_style = True
            self.style_content = ''

    def handle_endtag(self, tag):
        if tag == 'script':
            cleaned_script = self.remove_js_css_comments(self.script_content)
            self.output.append(cleaned_script)
            self.output.append(f'</{tag}>')
            self.in_script = False
        elif tag == 'style':
            cleaned_style = self.remove_js_css_comments(self.style_content)
            self.output.append(cleaned_style)
            self.output.append(f'</{tag}>')
            self.in_style = False
        else:
            self.output.append(f'</{tag}>')

    def handle_data(self, data):
        if self.in_script:
            self.script_content += data
        elif self.in_style:
            self.style_content += data
        else:
            self.output.append(data)

    def handle_comment(self, data):
        # Skip HTML comments
        pass

    def remove_js_css_comments(self, text):
        # Remove /* ... */ comments, including ones with *-prefixes on new lines
        text = re.sub(r'/\*[^*]*\*+(?:[^/*][^*]*\*+)*/', '', text, flags=re.DOTALL)

        # Remove // line comments not in strings
        def strip_line_comments(code):
            output_lines = []
            for line in code.splitlines():
                in_string = False
                escape = False
                for i, c in enumerate(line):
                    if c in ('"', "'") and not escape:
                        if not in_string:
                            in_string = c
                        elif in_string == c:
                            in_string = False
                    elif c == '\\':
                        escape = not escape
                        continue
                    if not in_string and line[i:i+2] == '//':
                        line = line[:i]
                        break
                    escape = False
                output_lines.append(line)
            return '\n'.join(output_lines)

        return strip_line_comments(text)

    def get_clean_html(self):
        return ''.join(self.output)

def remove_all_comments_from_html_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        parser = CommentStrippingHTMLParser()
        parser.feed(content)
        cleaned_html = parser.get_clean_html()

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(cleaned_html)

        print(f"Cleaned: {file_path}")
    except Exception as e:
        print(f"Couldn't Clean: {file_path} ({e})")

def clean_all_templates():
    for root, _, files in os.walk(DIR_PATH):
        for filename in files:
            if filename.endswith('.html'):
                file_path = os.path.join(root, filename)
                remove_all_comments_from_html_file(file_path)


clean_all_templates()
