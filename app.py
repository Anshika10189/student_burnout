from flask import Flask, render_template, request
import joblib
import numpy as np
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Load model and encoder
model = joblib.load("model.pkl")
encoder = joblib.load("encoder.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get input values
    study_hours = float(request.form["study_hours"])
    sleep_hours = float(request.form["sleep_hours"])
    stress_level = float(request.form["stress_level"])
    attendance = float(request.form["attendance"])
    assignments = float(request.form["assignments"])

    # Prediction
    data = np.array([[study_hours, sleep_hours, stress_level, attendance, assignments]])
    prediction = model.predict(data)
    result = encoder.inverse_transform(prediction)[0]

    # Confidence
    confidence = round(max(model.predict_proba(data)[0]) * 100, 2)

    # Recommendation
    if result == "Low":
        advice = "Excellent! Maintain your current study-life balance."
    elif result == "Medium":
        advice = "Take regular breaks, sleep well, and reduce stress."
    else:
        advice = "High burnout risk! Consider reducing workload, improving sleep, and talking to a mentor."

    # Create static folder
    if not os.path.exists("static"):
        os.makedirs("static")

    labels = ["Study", "Sleep", "Stress", "Attendance", "Assignments"]
    values = [study_hours, sleep_hours, stress_level, attendance, assignments]

    # ---------------- BAR CHART ----------------
    plt.figure(figsize=(6,4))
    plt.bar(labels, values)
    plt.title("Student Performance Overview")
    plt.tight_layout()
    plt.savefig("static/bar.png")
    plt.close()

    # ---------------- PIE CHART ----------------
    plt.figure(figsize=(5,5))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.title("Activity Distribution")
    plt.savefig("static/pie.png")
    plt.close()

    # ---------------- LINE CHART ----------------
    plt.figure(figsize=(6,4))
    plt.plot(labels, values, marker="o")
    plt.title("Performance Trend")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("static/line.png")
    plt.close()

    return render_template(
        "result.html",
        prediction=result,
        confidence=confidence,
        advice=advice
    )


if __name__ == "__main__":
    app.run(debug=True)