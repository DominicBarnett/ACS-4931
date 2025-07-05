# By Kami Bigdely
# Introduce explaining variable (alias extract variable)
# Reference: https://www.researchgate.net/publication/305768969_The_role_of_eye_characteristics_in_facial_beauty_likability_and_attractiveness
import math

# Background: You are a computer engineer trying to sift through many profiles to find your soulmate. 
# Unfortunately, there are too many profiles and it's getting tedious. You write a python script to 
# scrape profiles info (such as height, age, etc) and images (for image processing) to figure out 
# automatically who is attractive to you.

# Here is a part of the script:
# assuming you have extracted the following info from the profile's image.

# Eye measurements extracted from profile image (in various units)
eye_size = 0.47    # [cm^2] - Total eye area
eye_width = 24.2   # [mm] - Width of the eye
eye_height = 23.7  # [mm] - Height of the eye

# Iris measurements (colored part of the eye)
iris_width = 20.2  # [mm] - Width of the iris
iris_height = 19.7 # [mm] - Height of the iris

# Calculate derived measurements for attractiveness analysis
# Calculate iris area using ellipse formula: π * (width/2) * (height/2)
iris_area = math.pi * (iris_width / 2) * (iris_height / 2)

# Calculate eye aspect ratio (height/width) - indicates eye shape
eye_aspect_ratio = eye_height / eye_width

# Calculate ratio of iris area to total eye area - indicates iris prominence
iris_to_eye_area_ratio = iris_area / eye_size

# Check if the person meets attractiveness criteria based on eye characteristics
# Criteria based on research on facial attractiveness:
# - Eye size > 0.45 cm² (large eyes are considered attractive)
# - Iris to eye area ratio >= 0.69 (prominent iris is attractive)
# - Eye aspect ratio >= 0.59 (balanced eye proportions)
if eye_size > 0.45 and iris_to_eye_area_ratio >= 0.69 and eye_aspect_ratio >= 0.59:
    print("I'm sorry I wasn't part of your past, can I make it up by being in your future?")
