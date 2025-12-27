import matplotlib.pyplot as plt
from PIL import Image
import cv2 
import numpy as np

# single figure for all subplots
fig = plt.figure(figsize=(15, 5))
fig.suptitle('Comparison of Image Reading Methods', fontsize=16)

# Read an Image with PIL
pil_image = Image.open('image1.jpg')
# convert to np array
pil_numpy = np.array(pil_image)

# Read an Image with OpenCV
cv2_image = cv2.imread('image1.jpg')
#convert BGR to RGB
cv2_rgb = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)

# Display PIL image
ax1 = fig.add_subplot(131)
ax1.imshow(pil_numpy)
ax1.set_title('PIL: RGB Image')
ax1.axis('off')

# Display OpenCV BGR (incorrect colors)
ax2 = fig.add_subplot(132)
ax2.imshow(cv2_image)
ax2.set_title('OpenCV: Incorrect BGR Image')
ax2.axis('off')

# Display OpenCV RGB (correct colors)
ax3 = fig.add_subplot(133)
ax3.imshow(cv2_rgb)
ax3.set_title('OpenCV: Correct RGB Image')
ax3.axis('off')

plt.tight_layout()
plt.show()

# Print shape information
print("Image Shape:", cv2_image.shape)
print("PIL RGB Pixel Value:", pil_numpy[0, 0])
print("OpenCV BGR Pixel Value:", cv2_image[0, 0])
print("OpenCV RGB Pixel Value:", cv2_rgb[0, 0])