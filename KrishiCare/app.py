from flask import Flask, render_template, request
import os
from soil_model import predict_soil_type
from crop_database import get_crops, get_crops_by_season

app = Flask(__name__)

UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html', crops=None)

@app.route('/predict', methods=['POST'])
def predict():
    if 'soilImage' not in request.files:
        return "No file part"
    file = request.files['soilImage']
    if file.filename == '':
        return "No selected file"

    image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_soil.jpg')
    file.save(image_path)

    soil_type = predict_soil_type(image_path)
    location = request.form.get('location', 'default')
    crops = get_crops(location, soil_type)

    return render_template('index.html', soil_type=soil_type, crops=crops)

@app.route('/season', methods=['POST'])
def season():
    season = request.form.get('season')
    crops = get_crops_by_season(season)
    return render_template('index.html', crops=crops, season=season)

if __name__ == '__main__':
    app.run(debug=True)
image_path = os.path.join("static", "uploaded_soil.jpg")
file.save(image_path)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
