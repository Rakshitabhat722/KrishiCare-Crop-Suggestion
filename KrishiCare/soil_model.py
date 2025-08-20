def predict_soil_type(image_path):
    import cv2
    import numpy as np

    img = cv2.imread(image_path)
    if img is None:
        return "Unknown"

    avg_color_per_row = np.average(img, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)

    blue, green, red = avg_color

    if red > green and red > blue:
        return "red soil"
    elif green > red and green > blue:
        return "black soil"
    else:
        return "loamy soil"