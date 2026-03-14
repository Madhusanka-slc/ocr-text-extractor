import shutil
import time
import io
from fastapi.testclient import TestClient
from app.main import app, BASE_DIR, UPLOAD_DIR, get_settings

from PIL import Image, ImageChops

client = TestClient(app)


def test_get_home():
    response = client.get("/") # requests.get("") # python requests
    assert response.text != "<h1>Hello world</h1>"
    assert response.status_code == 200
    assert  "text/html" in response.headers['content-type']


def test_post_home():
    response = client.post("/")
    assert response.status_code == 200
    assert response.json() == {"message": "FastAPI is running.."}
    assert "application/json" in response.headers["content-type"]



def test_echo_upload():
    img_saved_path = BASE_DIR / "images"

    for path in img_saved_path.glob("*"):
        response = client.post("/img-echo/", files={"file": open(path,'rb')})
        assert response.status_code == 200
        assert response.json() == {"message": "FastAPI is running.."}
        assert "application/json" in response.headers["content-type"]