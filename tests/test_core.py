# tests/test_core.py
"""Tests for the core module."""

import pytest
import numpy as np
from my_library.core import main_function, process_data

def test_main_function():
    """Test main_function with sample data."""
    # Setup
    sample_input = np.random.random((100, 100, 3))
    
    # Execute
    result = main_function(sample_input)
    
    # Assert
    assert result is not None
    # Add more specific assertions for your function

def test_process_data():
    """Test process_data with sample parameters."""
    # Setup
    sample_data = np.random.random((100, 100, 3))
    sample_params = {"param1": 0.5, "param2": 1.0}
    
    # Execute
    result = process_data(sample_data, sample_params)
    
    # Assert
    assert result is not None
    # Add more specific assertions for your function

