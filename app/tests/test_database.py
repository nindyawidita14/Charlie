"""
NAME:          test_database.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          24/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Suite of tests for testing the dashboards database
               functionality.
"""

import unittest
from app import app
from app.database.controllers import Database

class DatabaseTests(unittest.TestCase):
    """Class for testing database functionality and connection."""
    def setUp(self):
        """Run prior to each test."""
        self.db_mod = Database()

    def tearDown(self):
        """Run post each test."""
        pass

    def test_get_total_number_items(self):
        with app.app_context():
            """Test that the total number of items returns the correct value."""
            self.assertEqual(self.db_mod.get_total_number_items(), 8218165, 'Test total items returns correct value')

    def test_get_average_act_cost(self):
        with app.app_context():
            """Test that the total number of items returns the correct value."""
            self.assertEqual(self.db_mod.get_average_act_cost(), 76.22, 'Test ACT cost returns correct value')
    
    def test_get_number_unique_items(self):
        with app.app_context():
            """Test that the total number of items returns the correct value."""
            self.assertEqual(self.db_mod.get_number_unique_items(), 836, 'Test unique items returns correct value')

    def test_get_percentage_of_Antibacterials(self):
        with app.app_context():
            """Test the percentage of Antibacterials(0501) in infection drugs"""
            self.assertEqual(self.db_mod.get_percentage_of_Antibacterials(), 78.32, 'Test unique items returns correct value')
    
    def test_get_percentage_of_Antifungal(self):
        with app.app_context():
            """Test the percentage of Antifungal(0502) in infection drugs"""
            self.assertEqual(self.db_mod.get_percentage_of_Antifungal(), 9.44, 'Test unique items returns correct value')

    def test_get_percentage_of_Antiviral(self):
        with app.app_context():
            """Test the percentage of anthelmintics(0503) in infection drugs"""
            self.assertEqual(self.db_mod.get_percentage_of_Antiviral(), 6.19, 'Test unique items returns correct value')

    def test_get_percentage_of_Antiprotozoal(self):
        with app.app_context():
            """Test the percentage of anthelmintics(0504) in infection drugs"""
            self.assertEqual(self.db_mod.get_percentage_of_Antiprotozoal(), 4.83, 'Test unique items returns correct value')

    def test_get_percentage_of_Anthelmintics(self):
        with app.app_context():
            """Test the percentage of anthelmintics(0505) in infection drugs"""
            self.assertEqual(self.db_mod.get_percentage_of_Anthelmintics(), 1.22, 'Test unique items returns correct value')

if __name__ == "__main__":
    unittest.main()