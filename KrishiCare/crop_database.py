def get_crops(location, soil_type):
    crop_data = {
        "loamy soil": ["Wheat", "Sugarcane", "Cotton"],
        "black soil": ["Cotton", "Soybean", "Sorghum"],
        "red soil": ["Millet", "Groundnut", "Rice"]
    }
    return crop_data.get(soil_type.lower(), ["No data available"])

def get_crops_by_season(season):
    season_crops = {
        "summer": ["Sunflower", "Cotton"],
        "rainy": ["Rice", "Sugarcane"],
        "winter": ["Wheat", "Mustard"]
    }
    return season_crops.get(season.lower(), ["No crops found for this season"])