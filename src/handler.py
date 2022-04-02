from fastapi import UploadFile
from skimage.io import imread
from io import BytesIO
import numpy as np
import urllib
from keras.preprocessing.image import array_to_img, img_to_array

from PIL import Image

def preprocess(img: np.ndarray) -> np.ndarray:
    img = array_to_img(img, scale=False)
    img = img.resize((224, 224))
    img = img_to_array(img)
    return img / 255.0


def handle_url(url: str) -> np.ndarray:
    try:
        img_data = imread(url)
    except Exception:
        req = urllib.request.Request(url, headers={"User-Agent": "Magic Browser"})
        con = urllib.request.urlopen(req)
        img_data = imread(con)
    processed_img = preprocess(img_data)
    img_array = np.array([processed_img])
    return img_array


def read_imagefile(file):
    file_bytes = BytesIO(file)
    image = Image.open(file_bytes)
    return image


def handle_file(file: UploadFile) -> np.ndarray:
    img_data = read_imagefile(file)
    processed_img = preprocess(img_data)
    img_array = np.array([processed_img])
    return img_array
