from flask import Flask, render_template, request
import os
from quantum_modules import detector, simulator, estimator

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            file = request.files.get('file')
            if not file or file.filename == '':
                return "<h3>No file selected. Please upload a valid file.</h3>"

            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            algo = detector.detect_algorithm(filepath)
            attack_type = simulator.simulate_attack(algo)
            time_estimate = estimator.estimate_time(algo)

            return f"""
            <h2>⚛️ Quantum Threat Prediction</h2>
            <p><strong>Detected Algorithm:</strong> {algo}</p>
            <p><strong>Simulated Quantum Attack:</strong> {attack_type}</p>
            <p><strong>Estimated Time to Breach:</strong> {time_estimate}</p>
            <p>✅ Analysis complete.</p>
            <a href="/">🔙 Back to upload</a>
            """
        except Exception as e:
            return f"<h3>Server error:</h3><pre>{str(e)}</pre>"
    return render_template("index.html")

if __name__ == '__main__':
    print("[INFO] ✅ Starting Quantum Threat Predictor on port 5000...")
    app.run(debug=True, port=5000)
