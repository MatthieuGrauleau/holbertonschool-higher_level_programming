#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unittest for max_integer"""
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_mat_at_middle(self):
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
    
    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
    
    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    
    def test_negative_and_positive(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
    
    def test_string(self):
        self.assertEqual(max_integer("test"), "t")
    
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
    
    def test_nothing(self):
        self.assertIsNone(max_integer([]))
        
    def test_no_list(self):
        with self.assertRaises(TypeError):
            max_integer(123)