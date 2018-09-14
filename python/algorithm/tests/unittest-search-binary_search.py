import unittest
from search import binary_search
import tests.data as data

class TestBinarySearch(unittest.TestCase):
    def test_binary_search_find_23(self):
        self.assertEqual(binary_search(data.good_data, 23), 23)

    def test_binary_search_find_777(self):
        self.assertIs(binary_search(data.good_data, 777), None)