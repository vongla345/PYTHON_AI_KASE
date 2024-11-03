# predict_digit.py
import tensorflow as tf
import numpy as np
import tkinter as tk
from PIL import Image, ImageGrab

model = tf.keras.models.load_model("mnist_model.h5")

class DigitRecognizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MNIST Digit Recognizer")
        
        self.canvas = tk.Canvas(self.root, width=200, height=200, bg="white")
        self.canvas.grid(row=0, column=0, pady=20)
        self.canvas.bind("<B1-Motion>", self.draw)
        
        self.predict_button = tk.Button(self.root, text="Dự đoán", command=self.predict_digit)
        self.predict_button.grid(row=1, column=0, pady=10)
        
        self.clear_button = tk.Button(self.root, text="Xoá", command=self.clear_canvas)
        self.clear_button.grid(row=2, column=0, pady=10)
        
        self.label = tk.Label(self.root, text="", font=("Arial", 20))
        self.label.grid(row=3, column=0, pady=10)
        
        self.last_x, self.last_y = None, None

    def draw(self, event):
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill="black", width=10)
        
        self.last_x, self.last_y = event.x, event.y

    def clear_canvas(self):
        self.canvas.delete("all")
        self.label.config(text="")
        self.last_x, self.last_y = None, None

    def predict_digit(self):
        x = self.root.winfo_rootx() + self.canvas.winfo_x()
        y = self.root.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        img = ImageGrab.grab().crop((x, y, x1, y1))
        
        img = img.resize((28, 28)).convert("L")
        img = np.array(img)
        img = img.reshape(1, 28, 28) / 255.0
        
        prediction = np.argmax(model.predict(img), axis=-1)
        self.label.config(text=f"Kết quả: {prediction[0]}")

root = tk.Tk()
app = DigitRecognizerApp(root)
root.mainloop()
