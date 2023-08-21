import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

# Create a canvas with a specified width and height
canvas_width = 800
canvas_height = 600
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Load the image
image = Image.open("fond.jpg")
image = image.resize((canvas_width, canvas_height), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image)

# Create a background image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

root.mainloop()
