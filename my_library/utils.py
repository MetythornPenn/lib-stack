# my_library/utils.py
"""Utility functions for the library."""

import os
import logging

logger = logging.getLogger(__name__)

def utility_function(input_var):
    """
    A utility function.
    
    Args:
        input_var: Input variable
        
    Returns:
        Processed variable
    """
    # Implementation
    return processed_var

def setup_logging(level=logging.INFO):
    """
    Set up logging configuration.
    
    Args:
        level: Logging level
    """
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )