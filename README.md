# 🎓 Student Performance Prediction System using Machine Learning

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4.0-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A complete Flask-based web application that predicts student final exam scores using Linear Regression machine learning algorithm. Features a modern, responsive UI with real-time predictions and performance categorization.

## Project Overview

This system uses Machine Learning (Linear Regression) to predict a student's final exam score based on:
- **Attendance** (0-100%)
- **Internal Marks** (0-50)
- **Assignment Score** (0-50)

The system also categorizes performance as:
- **Good**: Score >= 75
- **Average**: Score 50-74
- **Poor**: Score < 50

## Tech Stack

- **Python 3.10+**
- **Flask** - Web framework
- **pandas** - Data manipulation
- **numpy** - Numerical operations
- **scikit-learn** - Machine Learning library (Linear Regression)

## Project Structure

```
student-performance-prediction/
│
├── app.py                 # Flask application with routes
├── model.py               # ML model training and prediction
├── dataset.csv            # Training dataset (35 rows)
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
│
├── templates/
│   └── index.html        # Web interface (HTML form)
│
└── static/
    └── style.css         # Styling for web interface
```

## Dataset

The dataset (`dataset.csv`) contains the following columns:
- `Attendance`: Student attendance percentage (0-100)
- `InternalMarks`: Internal examination marks (0-50)
- `AssignmentScore`: Assignment scores (0-50)
- `FinalScore`: Final exam score (0-100) - Target variable

**Total Records**: 35 rows of realistic training data

## Installation

### Step 1: Install Python
Make sure you have Python 3.10 or higher installed on your system.

### Step 2: Install Dependencies
Open terminal/command prompt in the project directory and run:

```bash
pip install -r requirements.txt
```

This will install:
- Flask 3.0.0
- pandas 2.1.4
- numpy 1.26.2
- scikit-learn 1.4.0
- joblib 1.3.2

## How to Run

### Step 1: Navigate to Project Directory
```bash
cd student-performance-prediction
```

### Step 2: Run the Flask Application
```bash
python app.py
```

### Step 3: Open Browser
Open your web browser and visit:
```
http://localhost:5000
```

### Step 4: Use the Application
1. Enter **Attendance** percentage (0-100)
2. Enter **Internal Marks** (0-50)
3. Enter **Assignment Score** (0-50)
4. Click **"Predict Final Score"** button
5. View the predicted score and performance category

## How It Works

1. **Model Training**: 
   - The `model.py` file loads the dataset from `dataset.csv`
   - Splits data into training (80%) and testing (20%) sets
   - Trains a Linear Regression model
   - Saves the trained model as `trained_model.pkl`

2. **Web Application**:
   - Flask app (`app.py`) serves the web interface
   - On startup, it automatically trains the model if `trained_model.pkl` doesn't exist
   - The `/predict` route receives form data, validates inputs, and returns predictions

3. **Prediction**:
   - User inputs are validated (ranges: Attendance 0-100, Internal Marks 0-50, Assignment Score 0-50)
   - The trained model predicts the final score
   - Performance category is determined based on the predicted score

## Output Description

When you submit the form, the application displays:

1. **Predicted Final Score**: A percentage value (0-100) showing the expected final exam score
2. **Performance Category**: 
   - **Good** (Green badge): Score >= 75%
   - **Average** (Orange badge): Score 50-74%
   - **Poor** (Red badge): Score < 50%
3. **Input Summary**: Shows the values you entered for verification

## Example Usage

**Input:**
- Attendance: 85%
- Internal Marks: 40/50
- Assignment Score: 42/50

**Output:**
- Predicted Final Score: 82.5%
- Performance Category: Good

## Model Performance

The Linear Regression model achieves high accuracy (R² Score typically > 0.99) on the test dataset, indicating strong predictive capability.

## Features

✅ **Complete Error Handling**: Validates all inputs and handles errors gracefully  
✅ **User-Friendly Interface**: Clean, modern web design  
✅ **Automatic Model Training**: Model trains automatically on first run  
✅ **Performance Categorization**: Automatically categorizes student performance  
✅ **Responsive Design**: Works on desktop and mobile devices  
✅ **Beginner-Friendly Code**: Well-commented, easy to understand  

## Troubleshooting

**Issue**: ModuleNotFoundError  
**Solution**: Make sure all dependencies are installed using `pip install -r requirements.txt`

**Issue**: Port already in use  
**Solution**: Change the port in `app.py` from 5000 to another port (e.g., 5001)

**Issue**: Model not predicting correctly  
**Solution**: Delete `trained_model.pkl` and restart the application to retrain the model

## License

This project is created for educational purposes and viva demonstrations.

## Screenshots

### Main Interface
- Modern gradient design with animated background
- Intuitive input fields with real-time validation
- Smooth animations and transitions

### Prediction Results
- Large, clear score display
- Color-coded performance categories
- Detailed input summary

## Contributing

Contributions are welcome! Feel free to fork this project and submit pull requests.

## GitHub Setup

To push this project to GitHub, follow the instructions in [GIT_SETUP.md](GIT_SETUP.md)

## Author

Student Performance Prediction System - Machine Learning Project

---

⭐ **Star this repo if you find it helpful!**
