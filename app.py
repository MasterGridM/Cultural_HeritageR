from flask import Flask, render_template, send_from_directory
import os
import pandas as pd

app = Flask(__name__)

# Define folder and CSV path
MODELS_FOLDER = 'My3DModels'
CSV_FILE = 'merged_file_data.csv'

@app.route('/')
def index():
    # Read the CSV file into a DataFrame
    df = pd.read_csv(CSV_FILE)
    models_data = []
    
    # Iterate through each file in the models folder
    for filename in os.listdir(MODELS_FOLDER):
        if filename.lower().endswith('.glb'):
            # Find matching CSV row by "Exact File Name"
            row = df[df['Exact File Name'] == filename]
            if not row.empty:
                description = row.iloc[0]['Description']
                timeline = row.iloc[0]['Timeline/Era']
                proper_name = row.iloc[0]['Proper Name']
            else:
                description = 'No description available'
                timeline = 'No timeline available'
                proper_name = filename  # fallback to file name if Proper Name is missing
            
            models_data.append({
                'filename': filename,
                'description': description,
                'timeline': timeline,
                'proper_name': proper_name
            })
    
    # Render the museum-style template with the models data
    return render_template('index.html', models=models_data)

# Serve GLB files so they can be loaded by the model-viewer component
@app.route('/models/<path:filename>')
def models(filename):
    return send_from_directory(MODELS_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
