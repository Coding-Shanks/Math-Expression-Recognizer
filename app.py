import os
import cv2
import pytesseract
import numpy as np
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from werkzeug.utils import secure_filename
import re
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flash messages
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def preprocess_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    denoised = cv2.fastNlMeansDenoising(binary)
    return denoised


def extract_expression(image_path):
    processed_img = preprocess_image(image_path)
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789+-*/='
    text = pytesseract.image_to_string(processed_img, config=custom_config)
    return text.strip().replace('\n', '')


def validate_and_parse_expression(expression):
    pattern = r'^(\d+)\s*([+-])\s*(\d+)$'
    match = re.match(pattern, expression)
    if not match:
        raise ValueError("Invalid expression format. Please use format like '20 - 6' or '15 + 3'")
    num1, operator, num2 = match.groups()
    return int(num1), operator, int(num2)


def calculate_result(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    else:
        raise ValueError("Unsupported operator. Use + or -")


def process_math_image(image_path):
    try:
        expression = extract_expression(image_path)
        num1, operator, num2 = validate_and_parse_expression(expression)
        result = calculate_result(num1, operator, num2)
        return {
            'expression': f"{num1} {operator} {num2}",
            'result': result,
            'image_path': image_path.replace('static/', '')
        }
    except Exception as e:
        return {'error': str(e), 'image_path': image_path.replace('static/', '')}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            result = process_math_image(filepath)
            return render_template('index.html', result=result)

    return render_template('index.html', result=None)


if __name__ == '__main__':
    app.run(debug=True)