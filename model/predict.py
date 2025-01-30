import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pickle
import pandas as pd
from utils.validation import validate_input

# Load the trained model and vectorizer
with open("model/automation_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("model/vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

def predict_function(user_input):
    """Predicts the corresponding Java function for a given automation step."""
    if not validate_input(user_input):
        return "INVALID_STEP"

    X_test_vec = vectorizer.transform([user_input])
    prediction = model.predict(X_test_vec)
    print(f"Predicted for '{user_input}': {prediction[0]}")  # Debugging line to check prediction
    return prediction[0]

def generate_automation_script(user_steps):
    """Generates an automation script based on the user's input steps."""
    # Strip any extra spaces and quotes around the steps
    cleaned_steps = [step.strip().replace('"', '') for step in user_steps]
    
    predictions = [predict_function(step) for step in cleaned_steps]
    script = "\n".join([f"// {step}: {function}" for step, function in zip(cleaned_steps, predictions)])
    return script

def save_output_script(user_steps):
    """Generates a CSV file with predicted automation functions."""
    # Strip any extra spaces and quotes around the steps
    cleaned_steps = [step.strip().replace('"', '') for step in user_steps]
    
    predictions = [predict_function(step) for step in cleaned_steps]
    output_df = pd.DataFrame({"Step": cleaned_steps, "Function": predictions})
    output_file = "output/automation_script.csv"
    output_df.to_csv(output_file, index=False)
    return output_file

if __name__ == "__main__":
    user_steps = [
        "Open browser",
        "Login",
        "Click button",
        "Fill form",
        "Submit form",
        "Logout"
    ]
    
    output_file = save_output_script(user_steps)
    print(f"✅ Automation script saved at: {output_file}")
