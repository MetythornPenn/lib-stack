# tests/test_utils.py
"""Tests for the utilities module."""

import pytest
import logging
from my_library.utils import utility_function, setup_logging

def test_utility_function():
    """Test utility_function with sample input."""
    # Setup
    sample_input = "test"
    
    # Execute
    result = utility_function(sample_input)
    
    # Assert
    assert result is not None
    # Add more specific assertions for your function

def test_setup_logging():
    """Test setting up logging."""
    # Execute
    setup_logging(level=logging.DEBUG)
    
    # Assert
    logger = logging.getLogger()
    assert logger.level == logging.DEBUG