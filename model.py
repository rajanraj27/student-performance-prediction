import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
import os

def train_model():
    """Train the Linear Regression model on the dataset"""
    # Load dataset
    dataset_path = os.path.join(os.path.dirname(__file__), 'dataset.csv')
    df = pd.read_csv(dataset_path)
    
    # Features (X) and Target (y)
    X = df[['Attendance', 'InternalMarks', 'AssignmentScore']]
    y = df['FinalScore']
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create and train Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Save the trained model
    model_path = os.path.join(os.path.dirname(__file__), 'trained_model.pkl')
    joblib.dump(model, model_path)
    
    # Calculate and print accuracy (R² score)
    score = model.score(X_test, y_test)
    print(f"Model trained successfully! R² Score: {score:.4f}")
    
    return model

def load_model():
    """Load the trained model"""
    model_path = os.path.join(os.path.dirname(__file__), 'trained_model.pkl')
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        # Train model if it doesn't exist
        return train_model()

def predict_final_score(attendance, internal_marks, assignment_score):
    """Predict final score based on input features"""
    model = load_model()
    
    # Create input DataFrame with proper column names
    input_data = pd.DataFrame({
        'Attendance': [attendance],
        'InternalMarks': [internal_marks],
        'AssignmentScore': [assignment_score]
    })
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Ensure prediction is within valid range (0-100)
    prediction = max(0, min(100, prediction[0]))
    
    return round(prediction, 2)

if __name__ == "__main__":
    # Train the model when script is run directly
    train_model()
