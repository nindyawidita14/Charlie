import unittest
from flask import Flask
from flask_testing import TestCase
from app import app

class TotalDrugSpendTests(TestCase):
    """Class for testing the total drug spend tile."""

    def create_app(self):
        """Create and configure a new app instance for each test."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_total_drug_spend_tile(self):
        """Test the total drug spend tile."""
        response = self.client.get('/dashboard/home/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Total drug spend:', response.data)
        self.assertIn(b'This is the total amount spend in drugs cost.', response.data)
        self.assertIn(b'fas fa-info-circle', response.data)
        self.assertIn(b'fas fa-pound-sign fa-2x text-gray-300', response.data)
        self.assertRegex(response.data.decode('utf-8'), r'£\d+(\.\d{1,2})?')

if __name__ == "__main__":
    unittest.main()