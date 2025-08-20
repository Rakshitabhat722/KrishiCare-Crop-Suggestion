import cv2
import os

# Simulated soil type result (in real use, replace this with your ML model)
soil_type = "Loamy"  # Assume detected from image

# Get user's location
location = input("Enter your location (e.g., Sirsi, Bangalore): ").strip().lower()

# Simulated database: (location, soil_type) → list of crops
crop_db = {
    ("sirsi", "loamy"): ["Arecanut", "Paddy", "Banana"],
    ("bangalore", "red"): ["Ragi", "Groundnut", "Sunflower"],
    ("mysore", "black"): ["Cotton", "Jowar", "Tobacco"],
    ("hubli", "sandy"): ["Groundnut", "Millet", "Maize"],
}

# Construct full image path
image_path = r"C:\Users\bhatr\OneDrive\รูปภาพ\SoilImages\soil.jpg"

# Load and display image
img = cv2.imread(image_path)
if img is None:
    print("Failed to load image. Check path or file format.")
else:
    cv2.imshow("Uploaded Soil Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(f"\n📍 Location: {location.title()}")
    print(f"🧪 Detected Soil Type: {soil_type}")

    # Get crop suggestion
    key = (location, soil_type.lower())
    if key in crop_db:
        print("🌾 Suggested Crops for Your Region and Soil:")
        for crop in crop_db[key]:
            print(" -", crop)
    else:
        print("❌ Sorry! No crop data found for this location and soil type.")
