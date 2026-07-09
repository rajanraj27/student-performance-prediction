from flask import Flask, render_template, request, jsonify
from model import predict_final_score, train_model
import os

app = Flask(__name__)

# Train model on startup if it doesn't exist
if not os.path.exists('trained_model.pkl'):
    print("Training model...")
    train_model()

def get_performance_category(score):
    """Determine performance category based on final score"""
    if score >= 75:
        return "Good"
    elif score >= 50:
        return "Average"
    else:
        return "Poor"

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests"""
    try:
        # Get input data from form
        attendance = float(request.form.get('attendance'))
        internal_marks = float(request.form.get('internal_marks'))
        assignment_score = float(request.form.get('assignment_score'))
        
        # Validate input ranges
        if not (0 <= attendance <= 100):
            return jsonify({'error': 'Attendance must be between 0 and 100'}), 400
        if not (0 <= internal_marks <= 50):
            return jsonify({'error': 'Internal Marks must be between 0 and 50'}), 400
        if not (0 <= assignment_score <= 50):
            return jsonify({'error': 'Assignment Score must be between 0 and 50'}), 400
        
        # Make prediction
        predicted_score = predict_final_score(attendance, internal_marks, assignment_score)
        
        # Get performance category
        performance_category = get_performance_category(predicted_score)
        
        return jsonify({
            'success': True,
            'predicted_score': predicted_score,
            'performance_category': performance_category,
            'attendance': attendance,
            'internal_marks': internal_marks,
            'assignment_score': assignment_score
        })
    
    except ValueError:
        return jsonify({'error': 'Please enter valid numbers'}), 400
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
