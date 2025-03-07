# 🧮 Math Expression Recognizer

A Flask web application that allows users to upload images of handwritten mathematical expressions and extracts the expression using OCR, then evaluates the result. 

## 📂 Repository Name
**math-expression-recognizer**

## 📜 Description
This project provides a simple web-based interface where users can upload an image containing a handwritten mathematical expression (e.g., "20 - 6"). The application processes the image using OpenCV and Tesseract OCR to extract the expression, validates it, and computes the result. The extracted expression and result are then displayed on the webpage along with the uploaded image.

## 🚀 Features
- ✅ Upload interface for images
- 🔍 OCR-based text extraction
- ✏️ Handwritten mathematical expression recognition
- ➕➖ Supports addition and subtraction operations
- 📸 Displays uploaded images and results
- ⚠️ Flash messages for error handling
- 🎨 Styled with CSS for a user-friendly interface
- 🔐 Secure file upload handling

## 🏗️ Project Structure
```
math-expression-recognizer/
├── static/
│   ├── css/
│   │   └── style.css
│   └── uploads/
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
└── README.md
```

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Coding-Shanks/math-expression-recognizer.git
   cd math-expression-recognizer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install Tesseract OCR (required for text extraction)
   - Windows: [Download Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
   - Linux:
     ```bash
     sudo apt install tesseract-ocr
     ```

## 🚀 Running the Application
1. Start the Flask app:
   ```bash
   python app.py
   ```
2. Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```
3. Upload an image containing a handwritten math expression and get the computed result!

## 📝 How to Use
1. Visit the web page.
2. Click "Choose File" and select an image with a handwritten math expression (e.g., "20 - 6").
3. Click "Calculate".
4. See the extracted expression, result, and uploaded image displayed below.

## 📦 Dependencies
- Flask 🐍
- OpenCV 👁️
- Tesseract OCR 🔍
- NumPy ➗
- Pillow 🖼️
- Werkzeug 🔐

## ⚠️ Notes
- The app currently supports only addition (+) and subtraction (-).
- Handwritten expressions should be clear and legible for best results.
- Uploaded images are stored in `static/uploads/`.
- Runs in debug mode for development; remove `debug=True` for production.

## 🤝 Contributing
Pull requests are welcome! If you have any improvements or bug fixes, feel free to fork the repo and submit a PR.

## 📜 License
This project is open-source and available under the MIT License.

---
💡 **Developed with using Flask, OpenCV, and Tesseract OCR**

