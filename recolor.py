import cv2
import numpy as np
from pyciede2000 import ciede2000
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color

def rgb_to_cielab(rgb_color):
    # Convert RGB to sRGBColor object
    rgb = sRGBColor(rgb_color[0] / 255, rgb_color[1] / 255, rgb_color[2] / 255)
    # Convert sRGBColor to LabColor
    lab_color = convert_color(rgb, LabColor)
    # Access LabColor values
    l_value = lab_color.lab_l
    a_value = lab_color.lab_a
    b_value = lab_color.lab_b
    return (l_value, a_value, b_value)

def get_color_difference(color1, color2):
    res = ciede2000(rgb_to_cielab(color1), rgb_to_cielab(color2))
    return res['delta_E_00']

def find_nearest_color(original_color):
    # List of your provided colors in RGB format
    provided_colors = [(175, 181, 199),(0, 87, 166),(255, 255, 255),(255, 224, 1),(255, 126, 20),(179, 0, 6),(33, 33, 33),(196, 224, 0),(95, 38, 131),(227, 160, 91),(106, 206, 224),(255, 129, 114)]
    # Sample pixel color in BGR format (OpenCV's default)
    pixel_color = original_color
    # Calculate Euclidean distance between the pixel color and each provided color in RGB space
    distances = [get_color_difference(color, pixel_color) for color in provided_colors]
    # Find the index of the nearest color
    nearest_color_index = np.argmin(distances)
    nearest_color = provided_colors[nearest_color_index]
    # print("Nearest color:", nearest_color)
    return nearest_color

src = 'src\\'
img = 'kaido.jpg'

# Read the image
image = cv2.imread(src+img)

# Define the pixelation factor
pixelation_width = image.shape[0] // 5
pixelation_height = image.shape[1] // 5

# Resize the image down and then up to pixelate
height, width = image.shape[:2]
temp = cv2.resize(image, (pixelation_width, pixelation_height), interpolation=cv2.INTER_LINEAR)
pixelated = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

# Get the height and width of the image
height, width = pixelated.shape[:2]

# # Iterate over each row of pixels
# for y in range(height):
#     # Iterate over each pixel in the current row
#     for x in range(width):
#         # Set green and blue components to zero, keep red at its maximum
#         image[y, x] = find_nearest_color(image[y, x])  # BGR format

# Iterate over each 5x5 block
for y in range(0, height, 5):
    for x in range(0, width, 5):
        # Set the color of each pixel in the block to the replacement color
        pixelated[y:y+5, x:x+5] = find_nearest_color(pixelated[y, x])

tgt = 'tgt\\'

# Save or display the recolored image
cv2.imwrite(tgt+img, pixelated)

