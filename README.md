# AI Cyber Threat Detector

## Project Overview
AI Cyber Threat Detector is an advanced anomaly detection system that utilizes machine learning techniques to identify suspicious network activities. This project employs the Isolation Forest algorithm to detect potential cyber threats in real-time by analyzing network packet data. The system integrates packet capture, data preprocessing, and anomaly detection into a streamlined workflow.

## Features
- **Real-time Packet Capture**: Uses Scapy to sniff network traffic and extract essential packet details.
- **Data Processing**: Converts raw packet data into structured CSV format for analysis.
- **Anomaly Detection**: Employs an Isolation Forest model to classify network packets as normal or anomalous.
- **Web Interface**: Provides a Flask-based API for model training and anomaly detection.
- **CSV Data Generation**: Simulates network traffic for testing purposes.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Flask
- Pandas
- Scikit-learn
- Scapy
- Joblib

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Hackerpoorna/AI-Cyber-Threat-Detector.git
   cd AI-Cyber-Threat-Detector
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the packet generator to create sample network data:
   ```bash
   python main.py
   ```
4. Train the anomaly detection model:
   ```bash
   python app.py
   ```
   - Use the `/train` API endpoint to train the model.
   - Use the `/anomalies` API endpoint to detect anomalies in captured packets.

## Usage
- Start the Flask application:
  ```bash
  python app.py
  ```
- Use the web interface or API endpoints to analyze network traffic.
- Capture real-time packets:
  ```bash
  python capture_packets.py
  ```

## Team Members
- [**Poornachandra Vatambedu**](https://github.com/Hackerpoorna) (Leader)
- [Team Member 1](https://github.com/example1)
- [Team Member 2](https://github.com/example2)
- [Team Member 3](https://github.com/example3)
- [Team Member 4](https://github.com/example4)
- [Team Member 5](https://github.com/example5)

## GitHub Repository
[AI Cyber Threat Detector](https://github.com/Hackerpoorna/AI-Cyber-Threat-Detector)



