import numpy as np
import cv2
import matplotlib.pyplot as plt

def Canny_function(img, weak_th=None, strong_th=None):
    """
   Implementation of Canny Edge Detection Algorithm
    
    Parameters:
    -----------
    img : numpy array
        Input BGR image
    weak_th : float
        Weak threshold for edge detection (default: 10% of max gradient)
    strong_th : float
        Strong threshold for edge detection (default: 50% of max gradient)
    
    Returns:
    --------
    final_edges : numpy array
        Binary image with detected edges
    """
    
    # Step 1: Convert to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Get image dimensions
    height, width = img_gray.shape
    
    # Step 2: Apply Gaussian blur to reduce noise
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 1.4)
    
    # Step 3: Calculate gradients using Sobel operator
    # Gradient in X direction (vertical edges)
    gx = cv2.Sobel(np.float32(img_blur), cv2.CV_64F, 1, 0, 3)
    # Gradient in Y direction (horizontal edges)
    gy = cv2.Sobel(np.float32(img_blur), cv2.CV_64F, 0, 1, 3)
    
    # Step 4: Calculate gradient magnitude and direction
    #Magnitude: mag = √(gx² + gy²)
    #Direction: ang = arctan(gy / gx)
    mag, ang = cv2.cartToPolar(gx, gy, angleInDegrees=True)
    
    # Step 5: Calculate thresholds
    max_mag = np.max(mag)
    
    if weak_th is None:
        weak_th = max_mag * 0.1
    if strong_th is None:
        strong_th = max_mag * 0.5
    
    # Step 6: Non-Maximum Suppression
    # Keep only local maxima in gradient direction
    mag_suppressed = np.copy(mag)
    
    '''
    Angle Range    Direction    Check Neighbors
    0° - 22.5°     Horizontal   Left & Right    -> grad close to 0°/180° Horizontal
    22.5° - 67.5°  Diagonal /   Top-left & Bottom-right -> grad close to 45° diagonal
    67.5° - 112.5° Vertical     Top & Bottom -> grad close to 90° vertical 
    112.5° - 157.5° Diagonal \  Top-right & Bottom-left -> 135° diagonal
    '''

    for i_y in range(1, height - 1): 
        for i_x in range(1, width - 1):
            grad_ang = ang[i_y, i_x]
            
            # Normalize angle to 0-180 degrees
            grad_ang = abs(grad_ang - 180) if abs(grad_ang) > 180 else abs(grad_ang)
            
            if (0 <= grad_ang < 22.5) or (157.5 <= grad_ang <= 180):
                # Horizontal edge (0°/180°) - check left and right
                neighb_1_x, neighb_1_y = i_x - 1, i_y
                neighb_2_x, neighb_2_y = i_x + 1, i_y
                
            elif 22.5 <= grad_ang < 67.5:
                # Diagonal edge (45°) - check diagonal
                neighb_1_x, neighb_1_y = i_x - 1, i_y - 1
                neighb_2_x, neighb_2_y = i_x + 1, i_y + 1
                
            elif 67.5 <= grad_ang < 112.5:
                # Vertical edge (90°) - check up and down
                neighb_1_x, neighb_1_y = i_x, i_y - 1
                neighb_2_x, neighb_2_y = i_x, i_y + 1
                
            else:  # 112.5 <= grad_ang < 157.5
                # Diagonal edge (135°) - check other diagonal
                neighb_1_x, neighb_1_y = i_x - 1, i_y + 1
                neighb_2_x, neighb_2_y = i_x + 1, i_y - 1
            
            # Suppress if current pixel is not a local maximum
            if (mag[i_y, i_x] < mag[neighb_1_y, neighb_1_x]) or \
               (mag[i_y, i_x] < mag[neighb_2_y, neighb_2_x]):
                mag_suppressed[i_y, i_x] = 0
    
    # Step 7: Double Thresholding
    # Classify pixels as: 0 (non-edge), 1 (weak edge), 2 (strong edge)
    ids = np.zeros_like(img_gray, dtype=np.uint8)
    
    for i_y in range(height):
        for i_x in range(width):
            grad_mag = mag_suppressed[i_y, i_x]
            
            if grad_mag < weak_th:
                # Non-edge
                mag_suppressed[i_y, i_x] = 0
                ids[i_y, i_x] = 0
            elif weak_th <= grad_mag < strong_th:
                # Weak edge
                ids[i_y, i_x] = 1
            else:  # grad_mag >= strong_th
                # Strong edge
                ids[i_y, i_x] = 2
    
    # Step 8: Edge Tracking by Hysteresis
    # Keep weak edges only if connected to strong edges
    final_edges = np.copy(ids)
    
    for i_y in range(1, height - 1):
        for i_x in range(1, width - 1):
            if ids[i_y, i_x] == 1:  # Weak edge
                # Check 8-connected neighbors
                has_strong_neighbor = False
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if dy == 0 and dx == 0:
                            continue
                        if ids[i_y + dy, i_x + dx] == 2:  # Strong edge
                            has_strong_neighbor = True
                            break
                    if has_strong_neighbor:
                        break
                
                if has_strong_neighbor:
                    final_edges[i_y, i_x] = 2  # Promote to strong edge
                else:
                    final_edges[i_y, i_x] = 0  # Suppress weak edge
    
    # Convert to binary (0 or 255)
    final_edges = (final_edges == 2).astype(np.uint8) * 255
    
    return final_edges, mag, ang, mag_suppressed, ids

def visualize_canny_steps(image_path):
    """Visualize all steps of Canny edge detection"""
    
    img = cv2.imread(image_path)
    
    if img is None:
        print(f"Error: Could not load image from {image_path}")
        return
    
    # Apply custom Canny function
    final_edges, mag, ang, mag_suppressed, ids = Canny_function(img)
    
    # Compare with OpenCV's Canny
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    opencv_canny = cv2.Canny(img_gray, 50, 150)
    
    # Create visualization
    fig, axes = plt.subplots(2, 4, figsize=(20, 10))
    fig.suptitle('Canny Edge Detection - Step by Step', fontsize=16, fontweight='bold')
    
    # Row 1: Intermediate steps
    axes[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    axes[0, 0].set_title('1. Original Image')
    axes[0, 0].axis('off')
    
    axes[0, 1].imshow(mag, cmap='gray')
    axes[0, 1].set_title('2. Gradient Magnitude')
    axes[0, 1].axis('off')
    
    axes[0, 2].imshow(ang, cmap='hsv')
    axes[0, 2].set_title('3. Gradient Direction')
    axes[0, 2].axis('off')
    
    axes[0, 3].imshow(mag_suppressed, cmap='gray')
    axes[0, 3].set_title('4. After Non-Max Suppression')
    axes[0, 3].axis('off')
    
    # Row 2: Thresholding and final results
    axes[1, 0].imshow(ids, cmap='gray', vmin=0, vmax=2)
    axes[1, 0].set_title('5. Double Threshold\n(0=none, 1=weak, 2=strong)')
    axes[1, 0].axis('off')
    
    axes[1, 1].imshow(final_edges, cmap='gray')
    axes[1, 1].set_title('6. Custom Canny Result')
    axes[1, 1].axis('off')
    
    axes[1, 2].imshow(opencv_canny, cmap='gray')
    axes[1, 2].set_title('7. OpenCV Canny Result')
    axes[1, 2].axis('off')
    
    # Difference
    diff = cv2.absdiff(final_edges, opencv_canny)
    axes[1, 3].imshow(diff, cmap='gray')
    axes[1, 3].set_title('8. Difference')
    axes[1, 3].axis('off')
    
    plt.tight_layout()
    plt.show()


# Run the visualization
if __name__ == "__main__":
    visualize_canny_steps('image.jpg')