import cv2
import numpy as np

def find_nearest_color(original_color):
    # List of your provided colors in RGB format
    provided_colors = [(129, 83, 232),(208, 153, 75),(73, 73, 71),(199, 200, 191),(240, 200, 0),(179, 114, 227)]
    # Sample pixel color in BGR format (OpenCV's default)
    pixel_color = original_color
    # Calculate Euclidean distance between the pixel color and each provided color in RGB space
    distances = [np.linalg.norm(np.array(pixel_color) - np.array(color)) for color in provided_colors]
    # Find the index of the nearest color
    nearest_color_index = np.argmin(distances)
    nearest_color = provided_colors[nearest_color_index]
    # print("Nearest color:", nearest_color)
    return nearest_color

image = cv2.imread('mona-lisa-pixelated.jpg')

# Get the height and width of the image
height, width = image.shape[:2]

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
        image[y:y+5, x:x+5] = find_nearest_color(image[y, x])

# Save or display the recolored image
cv2.imwrite('recolored-mona-list.jpg', image)

