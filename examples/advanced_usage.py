# examples/advanced_usage.py
"""Advanced usage examples for my_library."""

import os
import torch
import numpy as np
import cv2
from my_library import main_function, process_data, utility_function

def advanced_example():
    """Demonstrate more advanced usage of the library."""
    # Set up device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    # Create sample data
    sample_img = np.random.randint(0, 255, (500, 500, 3), dtype=np.uint8)
    
    # Define custom parameters
    params = {
        "threshold": 0.75,
        "max_iterations": 100,
        "use_gpu": torch.cuda.is_available()
    }
    
    # Process with custom parameters
    result = process_data(sample_img, parameters=params)
    
    # Save the result
    output_path = "advanced_result.jpg"
    cv2.imwrite(output_path, result)
    
    print(f"Advanced processing complete. Result saved to {output_path}")
    
    # Apply utility function
    utility_result = utility_function("advanced_sample")
    print(f"Utility function result: {utility_result}")

if __name__ == "__main__":
    advanced_example()