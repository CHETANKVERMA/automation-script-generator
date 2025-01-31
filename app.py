from flask import Flask, render_template, request, send_file
import os
from model.predict import save_output_script

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Your HTML form

@app.route('/generate_script', methods=['POST'])
def generate_script():
    if request.method == 'POST':
        user_steps = request.json['steps']  # Get the user steps as JSON
        output_file = save_output_script(user_steps)  # Your ML script generation logic
        return send_file(output_file, as_attachment=True)  # Send the file for download

# No app.run here, we use Gunicorn to serve the app in production
