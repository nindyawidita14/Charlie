import unittest
from flask import Flask
from flask_testing import TestCase
from app import app

class TopPrescribedItemsTests(TestCase):
    """Class for testing the top prescribed items tile."""

    def create_app(self):
        """Create and configure a new app instance for each test."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_top_prescribed_items_tile(self):
        """Test the top prescribed items tile."""
        response = self.client.get('/dashboard/home/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'TOP PRESCRIBED ITEM:', response.data)
        self.assertIn(b'This is the top prescribed item, its count, and its percentage of all items.', response.data)
        self.assertIn(b'fas fa-info-circle', response.data)
        self.assertIn(b'fas fa-clipboard-list fa-2x text-gray-300', response.data)
        self.assertRegex(response.data.decode('utf-8'), r'\d+%')

if __name__ == "__main__":
    unittest.main()