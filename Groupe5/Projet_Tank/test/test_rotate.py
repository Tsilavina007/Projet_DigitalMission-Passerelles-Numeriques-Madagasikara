from PIL import Image

# Open the image file
image = Image.open("z.png")

# Rotate the image by 90 degrees clockwise
rotated_image = image.rotate(10)  # Specify the angle of rotation in degrees

# Save the rotated image to a new file
rotated_image.save("rotated_image.png")
