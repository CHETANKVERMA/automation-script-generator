# Automation Script Generator

## Overview
This project is a **Flask-based web application** that leverages **Machine Learning (Random Forest with TF-IDF)** to generate automation scripts based on user-provided steps. The model predicts corresponding automation functions and outputs them in a structured script format.

## Features
- **Web-based Interface**: Users can enter automation steps and download the generated script.
- **Machine Learning-based Prediction**: Uses a trained **Random Forest model** with **TF-IDF** vectorization to map input steps to automation functions.
- **Dynamic Script Generation**: Outputs structured Java-like automation scripts.
- **CSV-based Data Handling**: Loads sample automation steps from CSV files for model training.
- **Deployment Ready**: Can be deployed using **Render** or other hosting services.

## Tech Stack
| Component        | Technology Used |
|-----------------|----------------|
| Backend        | Flask (Python) |
| Machine Learning | Random Forest, TF-IDF (Scikit-learn) |
| Frontend       | HTML, CSS, JavaScript |
| Data Handling  | Pandas, CSV files |
| Model Deployment | Pickle (for model persistence) |
| Version Control | Git & GitHub |
| Deployment | Render (Free Tier) |

## Installation & Setup
### Prerequisites
- Python 3.8+
- Git
- Virtual Environment (Recommended)
- Flask & Required Dependencies
- Render/GitHub for deployment

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/automation-script-generator.git
   cd automation-script-generator
   ```

2. **Create & Activate Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the ML Model**:
   ```bash
   python model/train_model.py
   ```

5. **Run the Application**:
   ```bash
   python main.py
   ```
   The app will be available at **http://127.0.0.1:5000**.

## Project Structure
```
automation_model/
│── data/                   # Input CSV files
│── output/                 # Generated automation scripts
│── model/                  # ML model files
│   ├── train_model.py      # Train ML model
│   ├── predict.py          # Predict automation functions
│── scripts/                # Java script generation
│── utils/                  # Helper functions
│── templates/              # HTML files for UI
│── static/                 # CSS & JS files
│── main.py                 # Flask main application
│── requirements.txt        # Dependencies
│── README.md               # Documentation
```

## How It Works
1. The user enters automation steps on the web interface.
2. The ML model (trained using automation data) predicts corresponding automation functions.
3. The generated script is formatted and provided for download.
4. The backend uses Flask to process inputs and serve the response.

## Contributing
Feel free to fork this repository and submit pull requests with improvements!


