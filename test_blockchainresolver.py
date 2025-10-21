# test_blockchainresolver.py
"""
Tests for BlockchainResolver module.
"""

import unittest
from blockchainresolver import BlockchainResolver

class TestBlockchainResolver(unittest.TestCase):
    """Test cases for BlockchainResolver class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockchainResolver()
        self.assertIsInstance(instance, BlockchainResolver)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockchainResolver()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
