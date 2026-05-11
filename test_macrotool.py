# test_macrotool.py
"""
Tests for MacroTool module.
"""

import unittest
from macrotool import MacroTool

class TestMacroTool(unittest.TestCase):
    """Test cases for MacroTool class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MacroTool()
        self.assertIsInstance(instance, MacroTool)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MacroTool()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
