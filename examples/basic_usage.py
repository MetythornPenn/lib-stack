# examples/basic_usage.py
"""Basic usage examples for my_library."""

import numpy as np
import cv2
from my_library import main_function, utility_function

def basic_example():
    """Demonstrate the basic usage of the library."""
    # Load an image (you could replace this with your own sample image)
    img = np.random.randint(0, 255, (300, 300, 3), dtype=np.uint8)
    
    # Process the image using the main function
    processed_img = main_function(img)
    
    # Display the result
    cv2.imshow("Original", img)
    cv2.imshow("Processed", processed_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    print("Basic example completed successfully!")

if __name__ == "__main__":
    basic_example()

