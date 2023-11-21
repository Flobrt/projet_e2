import os
import numpy as np
from PIL import Image
from app_flask import app
from flask import request, send_from_directory, render_template, url_for, redirect
from keras.preprocessing import image
from tensorflow.keras.models import load_model
from keras.applications.imagenet_utils import preprocess_input
from ultralytics import YOLO
import cv2


# Route pour la page principale
@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        if "file1" not in request.files:
            return "There is no file1 in form!"
        try:
            file1 = request.files["file1"]
            path = os.path.join(app.config["UPLOAD_FOLDER"], file1.filename)
            filename = file1.filename
            file1.save(path)
        except:
            return render_template('index.html', error="No file selected")

        # # Charger le modèle
        # model = load_model('./best_model.h5')
        
        # # Prédiction
        # # Charger l'image avec PIL
        # img = Image.open(path) 
        # # img = image.load_img(path, target_size=(256, 256))
        # img_array = image.img_to_array(img)
        # img_array = preprocess_input(img_array)
        # img_array = np.expand_dims(img_array, axis=0)
        
        # # Liste des labels possibles
        # class_label = ['Glioma', 'Meningioma', 'No tumor', 'Pituitary']
        
        # # Prédiction sur l'image insérée 
        # predictions = model.predict(img_array)
        # prediction = np.argmax(predictions)
        
        # # Je trouve la classe et le taux de probabilité associé 
        # predicted_class_label = class_label[prediction]
        # probabilities = np.max(predictions[0])
        
        # x=predicted_class_label
        # y=probabilities
         
        # return render_template('predict.html', x=x, y=y, path=path)  
        # retourner vers la view predict 
        return redirect(url_for('predict', path=path, filename=filename))
        
    return render_template('index.html')

# Route pour la page de prédiction
@app.route('/predict', methods=["GET"])
def predict():
    path = request.args.get('path', type=str)
    filename = request.args.get('filename', type=str)
    
    # Charger le modèle
    model = load_model('./best_model.h5')
    
    # Prédiction
    # img = Image.open(path) 
    img = image.load_img(path, target_size=(256, 256))
    img_array = image.img_to_array(img)
    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)
    
    # Liste des labels possibles
    class_label = ['Glioma', 'Meningioma', 'No tumor', 'Pituitary']
    
    # Prédiction sur l'image insérée 
    predictions = model.predict(img_array)
    prediction = np.argmax(predictions)
    
    # Je trouve la classe et le taux de probabilité associé 
    predicted_class_label = class_label[prediction]
    probabilities = np.max(predictions[0])
    
    x=predicted_class_label
    y=probabilities

    return render_template('predict.html', x=x, y=y, path=path, filename=filename)

@app.route('/yolo', methods=["GET"])
def yolo():
    # Load a model
    model = YOLO("yolov8n.yaml")  # build a new model from scratch
    model = YOLO("best.onnx", task='detect')  # load a pretrained model (recommended for training)

    model.conf = 0.7  # confidence threshold (0-1)
    model.iou = 0.7  # NMS IoU threshold (0-1)

    img_path = cv2.imread(request.args.get('path', type=str))
    result = model(img_path, project='app_flask/upload', name='predict', save=True)
    path_1 = f'.{result[0].save_dir}'

    # split path_1 by / and take the last element
    folder = path_1.split('/')[-1]
    return render_template('yolo.html', folder=folder)

@app.route('/app_flask/upload/<directory>/<filename>')
def uploaded_file2(directory, filename):
    # return send_from_directory("/home/florian/code/projet-e2/projet-e2-main/app_flask/upload/", filename)
    return send_from_directory(f"/Volumes/Macintosh HD - Données/Users/flo/Documents/Dev/projet_e2/projet-e2-main/app_flask/upload/{directory}", filename)

# Route pour la page de téléchargement
@app.route('/app_flask/upload/<filename>')
def uploaded_file(filename):
    # return send_from_directory("/home/florian/code/projet-e2/projet-e2-main/app_flask/upload/", filename)
    return send_from_directory("/Volumes/Macintosh HD - Données/Users/flo/Documents/Dev/projet_e2/projet-e2-main/app_flask/upload", filename)



# Route pour la page about
@app.route('/about')
def about():
    return render_template('about-us.html')