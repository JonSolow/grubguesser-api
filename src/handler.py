from skimage import io
import numpy as np
import urllib
from keras.preprocessing.image import array_to_img, img_to_array


def preprocess(img: np.ndarray) -> np.ndarray:
    img = array_to_img(img, scale=False)
    img = img.resize((224, 224))
    img = img_to_array(img)
    return img / 255.0


def handle_url(url: str) -> np.ndarray:
    try:
        img_data = io.imread(url)
    except Exception:
        req = urllib.request.Request(url, headers={"User-Agent": "Magic Browser"})
        con = urllib.request.urlopen(req)
        img_data = io.imread(con)
    processed_img = preprocess(img_data)
    img_array = np.array([processed_img])
    return img_array
