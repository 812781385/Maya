from flask import Flask, render_template
import random
import re
from bs4 import BeautifulSoup
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/get_random_line', methods=['GET'])
def get_random_line():
    file_path = random_txt_file()
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            random_line = random.choice(lines)
        cleaned_line = clean_line(random_line)
        return cleaned_line
    return "No txt files found in ./source folder"

def random_txt_file():
    import os
    folder_path = "./source"
    txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
    if txt_files:
        file_path = os.path.join(folder_path, random.choice(txt_files))
        return file_path
    return None

def clean_line(line):
    soup = BeautifulSoup(line, "html.parser")
    line_content = ''.join(soup.findAll(text=True))
    line_content = re.sub(r"^\d+、", "", line_content)
    line_content = line_content.strip()
    return line_content

if __name__ == '__main__':
    app.run()
