# test_artificialeaseltoolkit.py
"""
Tests for ArtificialEaselToolkit module.
"""

import unittest
from artificialeaseltoolkit import ArtificialEaselToolkit

class TestArtificialEaselToolkit(unittest.TestCase):
    """Test cases for ArtificialEaselToolkit class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArtificialEaselToolkit()
        self.assertIsInstance(instance, ArtificialEaselToolkit)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArtificialEaselToolkit()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
