import numpy as np
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
import os


class PredictionPipeline:
    def __init__(self, filename) -> None:
        self.file_name = filename

    def predict(self):

        model = load_model(os.path.join("artifacts", "training", "model.h5"))
        image_name = self.file_name
        test_image = image.load_img(image_name, target_size=(224, 224))
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = "Healty"
        else:
            prediction = "Coccidosis"

        return [{"image", prediction}]
