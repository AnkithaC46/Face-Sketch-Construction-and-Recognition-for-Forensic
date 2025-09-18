import os
import sqlite3
import datetime
from flask import Flask, render_template, request, url_for, send_from_directory, abort
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim


app = Flask(__name__, static_folder='static')
UPLOAD_FOLDER = 'static/uploads'
PHOTO_FOLDER = 'static/photos'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PHOTO_FOLDER, exist_ok=True)


def create_database():
    conn = sqlite3.connect('image_details.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS image_details (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            dob TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def populate_database(filename, name, age, dob):
    conn = sqlite3.connect('image_details.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO image_details (filename, name, age, dob)
        VALUES (?, ?, ?, ?)
    ''', (filename, name, age, dob))
    conn.commit()
    conn.close()

def add_sample_data():
    populate_database('photo.jpg', 'John Doe', 30, '1993-05-15')
    populate_database('photo1.jpg', 'Jane Smith', 25, '1998-02-20')
    populate_database('2.jpg', 'Alice Brown', 28, '1995-11-10')
    populate_database('Screenshot 2024-12-06 223656.png','srk',50,'1964-11-10')

def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Image at path {image_path} could not be loaded.")
    img = cv2.resize(img, (300, 300))  # Resize to a standard size
    return img

def calculate_ssim(image1, image2):
    return ssim(image1, image2)

def get_image_details(filename):
    conn = sqlite3.connect('image_details.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, age, dob FROM image_details WHERE filename = ?", (filename,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return {
            'name': result[0],
            'age': result[1],
            'dob': result[2]
        }
    return None

@app.route('/')
def home():
    return render_template('start.html')

@app.route('/upload', methods=['GET'])
def upload_page():
    return render_template('index.html')

@app.route('/create-sketch')
def create_sketch():
    return render_template('Face_Construct.html')

@app.route('/', methods=['POST'])
def index():
    if 'sketch' not in request.files:
        return "No file part"

    file = request.files['sketch']
    if file.filename == '':
        return "No selected file"

    if file:
        sketch_filename = f"sketch_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        sketch_path = os.path.join(UPLOAD_FOLDER, sketch_filename)
        file.save(sketch_path)

        try:
            sketch = preprocess_image(sketch_path)
        except ValueError as e:
            return str(e)

        best_match = None
        best_similarity = -1

        for filename in os.listdir(PHOTO_FOLDER):
            photo_path = os.path.join(PHOTO_FOLDER, filename)
            if os.path.isfile(photo_path):
                photo = preprocess_image(photo_path)
                similarity = calculate_ssim(sketch, photo)

                if similarity > best_similarity:
                    best_similarity = similarity
                    best_match = filename

        if best_match:
            image_details = get_image_details(best_match)
            result = {
                'sketch_path': sketch_filename,
                'photo_path': best_match,
                'similarity': round(best_similarity, 4),
                'details': image_details,
                'interpretation': "similar" if best_similarity > 0.1 else "not similar"
            }
            return render_template('result.html', result=result)
        else:
            return render_template('result.html', result=None)

@app.errorhandler(404)
def not_found_error(error):
    return "Image not found. Please check the path and try again.", 404

if __name__ == "__main__":
    create_database()
    add_sample_data()
    app.run(debug=True)

