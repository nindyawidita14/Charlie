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
from unittest.mock import patch

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

    @patch('app.database.controllers.db.session.query')
    def test_get_top_prescribed_item_with_percentage(self, mock_query):
         with app.app_context():
            # Mock the query results
            mock_query.return_value.group_by.return_value.order_by.return_value.limit.return_value.first.return_value = (
            'Omeprazole_Cap E/C 20mg', 226307
        )
            mock_query.return_value.scalar.return_value = 8218165  # Total items

            # Call the method
            result = self.db_mod.get_top_prescribed_item_with_percentage()

            # Verify the result
            self.assertEqual(result['top_item_name'], 'Omeprazole_Cap E/C 20mg')
            self.assertEqual(result['top_item_count'], 226307)
            self.assertAlmostEqual(result['percentage'], 2.75, places=2)


if __name__ == "__main__":
    unittest.main()