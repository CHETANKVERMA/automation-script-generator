import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import pickle
from utils.data_loader import load_data

nltk.download('punkt')

# Load data
data = load_data()
X_train = data["Step"]
y_train = data["Function"]

# Convert text to numerical features using TF-IDF
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_vec, y_train)

# Save the trained model and vectorizer
with open("model/automation_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

with open("model/vectorizer.pkl", "wb") as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

print("✅ Model training completed.")
