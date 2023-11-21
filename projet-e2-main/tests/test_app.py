import sys
import os
import pytest

# Ajouter le répertoire parent (my_project) à sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app_flask import app


# Créer un client de test pour l'application
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Tester la route principale
def test_main_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<form method="POST" enctype="multipart/form-data">' in response.data 
    
# Tester la route de prédiction
def test_predict_route(client):
    response = client.get('/predict')
    assert response.status_code == 200
    assert b'<h1>Result for MRI scan of a brain</h1>' in response.data  
    
# Tester la route about
def test_about_route(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b'''This website uses a custom trained model to diagnose MRI scans of human brains in order to recognise brain tumors in MRI scan of brains. If done early, death and other complications can be prevented.
    This serves as a tool and not actual medical advice! This tool can recognise different types of tumors as well; These include: Gioma, Pituitary and Meningioma''' in response.data
    
# Tester qu'une image est stockée dans le dossier uploads puis renvoyée
def test_uploard(client):
    data = {'file1': (open('tests/pic/normal.jpg', 'rb'), 'normal.jpg')}
    response = client.post('/', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b'<h1>Result for MRI scan of a brain</h1>' in response.data
    # Vérifier que l'image est bien stockée dans le dossier uploads
    assert os.path.isfile('app_flask/upload/normal.jpg') == True

if __name__ == '__main__':
    pytest.main()
