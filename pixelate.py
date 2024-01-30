import cv2

# Read the image
image = cv2.imread('mona-lisa.jpg')

# Define the pixelation factor
pixelation_width = image.shape[0] // 5
pixelation_height = image.shape[1] // 5

# Resize the image down and then up to pixelate
height, width = image.shape[:2]
temp = cv2.resize(image, (pixelation_width, pixelation_height), interpolation=cv2.INTER_LINEAR)
pixelated = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

# Save or display the pixelated image
cv2.imwrite('mona-lisa-pixelated.jpg', pixelated)
