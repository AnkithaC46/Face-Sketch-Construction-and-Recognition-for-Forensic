# Face Sketch Construction and Recognition for Forensic

## Overview
This project is a **Forensic Face Sketch Construction and Recognition** system designed to help law enforcement create accurate face sketches of suspects without requiring a forensic artist. It also matches the generated sketches with an existing criminal database using deep learning techniques.

## Features
- **Face Sketch Construction**: Drag-and-drop interface for assembling facial elements (eyes, nose, mouth, etc.).
- **Face Recognition**: Matches the generated sketch with a criminal database.
- **Backend Processing**: Utilizes Python Flask for handling recognition requests.
- **Deep Learning Model**: Uses the `face_recognition` library to compare face encodings.

## Technologies Used
- **Frontend**: JavaScript, HTML, CSS (for the sketch construction UI)
- **Backend**: Python (Flask framework)
- **Machine Learning**: `face_recognition` library
- **Database**: SQLite / PostgreSQL (for storing criminal records)

## Installation
### Prerequisites
- Python 3.11.6 (or later)
- Flask (`pip install flask`)
- face_recognition (`pip install face_recognition`)
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)
- Pillow (`pip install pillow`)

### Steps
1. **Clone the repository**
   ```sh
   git clone https://github.com/your-username/face-sketch-construction.git
   cd face-sketch-construction
   ```
2. **Set up a virtual environment **
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies**
  
4. **Run the application**
   ```sh
   python app.py
   ```
5. **Open in Browser**
   ```
   http://127.0.0.1:5000/
   ```

## Usage
1. Open the web app and use the drag-and-drop interface to create a suspect sketch.
2. Submit the sketch to match it with the criminal database.
3. The backend processes the image and returns possible matches with similarity scores.

## Future Enhancements
- **Enhance UI**: Improve the sketch construction interface with more facial elements.
- **Real-time Sketching**: Implement AI-based automated sketch generation.
- **Better Matching Algorithm**: Use CNN-based deep learning models for improved accuracy.
- **Cloud Deployment**: Deploy the project on AWS/GCP for wider accessibility.

## Research Paper
You can read the full technical paper related to this project here: [Technical Paper Link](https://ijsrem.com/download/face-sketch-construction-and-recognition-for-forensic/)

## Contributing
Feel free to fork this repository and submit pull requests with improvements!

