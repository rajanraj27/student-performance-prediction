import logging
import math
import os

from flask import Flask, jsonify, render_template, request
from model import predict_final_score

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024  # Requests are tiny; reject oversized bodies.

logging.basicConfig(level=os.environ.get("LOG_LEVEL", "INFO").upper())
logger = logging.getLogger(__name__)


def get_performance_category(score):
    """Determine performance category based on the predicted final score."""
    if score >= 75:
        return "Good"
    if score >= 50:
        return "Average"
    return "Poor"


@app.get("/")
def index():
    """Render the main page."""
    return render_template("index.html")


@app.get("/health")
def health():
    """Lightweight health check for hosting platforms."""
    return jsonify({"status": "ok"}), 200


@app.post("/predict")
def predict():
    """Validate submitted values and return a prediction."""
    try:
        attendance = float(request.form["attendance"])
        internal_marks = float(request.form["internal_marks"])
        assignment_score = float(request.form["assignment_score"])
    except (KeyError, TypeError, ValueError):
        return jsonify({"success": False, "error": "Please enter valid numbers in all fields."}), 400

    values = (attendance, internal_marks, assignment_score)
    if not all(math.isfinite(value) for value in values):
        return jsonify({"success": False, "error": "Please enter finite numeric values."}), 400

    if not 0 <= attendance <= 100:
        return jsonify({"success": False, "error": "Attendance must be between 0 and 100."}), 400
    if not 0 <= internal_marks <= 50:
        return jsonify({"success": False, "error": "Internal marks must be between 0 and 50."}), 400
    if not 0 <= assignment_score <= 50:
        return jsonify({"success": False, "error": "Assignment score must be between 0 and 50."}), 400

    try:
        predicted_score = predict_final_score(attendance, internal_marks, assignment_score)
    except Exception:
        logger.exception("Prediction failed")
        return jsonify({"success": False, "error": "Prediction is temporarily unavailable. Please try again."}), 500

    return jsonify({
        "success": True,
        "predicted_score": predicted_score,
        "performance_category": get_performance_category(predicted_score),
        "attendance": attendance,
        "internal_marks": internal_marks,
        "assignment_score": assignment_score,
    })


if __name__ == "__main__":
    # Local development only. Production uses Gunicorn (see Procfile).
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", "5000")), debug=False)
