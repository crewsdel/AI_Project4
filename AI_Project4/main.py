import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from tensorflow.keras.models import load_model


class ImageClassifierGUI:
    def __init__(self, model_path):
        self.model = load_model(model_path)
        self.img_height, self.img_width = 150, 150

        self.root = tk.Tk()
        self.root.title("Image Classifier")

        self.select_button = tk.Button(self.root, text="Select Image", command=self.classify_image)
        self.select_button.pack(pady=10)

        self.prediction_label = tk.Label(self.root, text="")
        self.prediction_label.pack()

        self.root.mainloop()

    def classify_image(self):
        file_path = filedialog.askopenfilename()
        if not file_path:
            return  # No file selected

        img = Image.open(file_path)
        img = img.resize((self.img_height, self.img_width))
        img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

        class_idx = np.argmax(self.model.predict(img_array), axis=1)[0]
        classes = ['glass', 'metal', 'paper', 'plastic']
        predicted_class = classes[class_idx]

        self.prediction_label.config(text=f'Predicted Class: {predicted_class}')


# Example usage
if __name__ == "__main__":
    gui = ImageClassifierGUI('recyclable_classifier.h5')
