from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

app = Flask(__name__)

# Global Variables
MODEL_FILE = "network_anomaly_model.pkl"
DATA_FILE = "packets.csv"


# Load model if available
def load_model():
    if os.path.exists(MODEL_FILE):
        return joblib.load(MODEL_FILE)
    return None


# Preprocess data
def preprocess_data(data_file):
    if not os.path.exists(data_file):
        raise FileNotFoundError(f"{data_file} not found. Please provide the file.")
    packet_df = pd.read_csv(data_file)
    
    # Check for required columns
    required_columns = ['src_ip', 'dst_ip', 'protocol', 'packet_length', 'timestamp']
    for col in required_columns:
        if col not in packet_df.columns:
            raise KeyError(f"Column '{col}' is missing from the data file.")
    
    # Feature engineering
    packet_df['src_ip_encoded'] = packet_df['src_ip'].astype('category').cat.codes
    packet_df['dst_ip_encoded'] = packet_df['dst_ip'].astype('category').cat.codes
    packet_df['protocol_encoded'] = packet_df['protocol'].astype('category').cat.codes
    features = packet_df[['src_ip_encoded', 'dst_ip_encoded', 'protocol_encoded', 'packet_length']]
    return features


# Train model
@app.route('/train', methods=['POST'])
def train_model():
    try:
        features = preprocess_data(DATA_FILE)
        model = IsolationForest(contamination=0.01, random_state=42)
        model.fit(features)
        joblib.dump(model, MODEL_FILE)
        return jsonify({"message": "Model trained successfully and saved."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Detect anomalies
@app.route('/anomalies', methods=['GET'])
def detect_anomalies():
    try:
        model = load_model()
        if model is None:
            raise FileNotFoundError("Model file not found. Train the model first.")

        features = preprocess_data(DATA_FILE)
        anomalies = model.predict(features)
        results = pd.DataFrame(features)
        results['anomaly'] = anomalies
        anomalies_detected = results[results['anomaly'] == -1]

        return jsonify({"anomalies": anomalies_detected.to_dict(orient='records')}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Home route to render HTML page
@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
