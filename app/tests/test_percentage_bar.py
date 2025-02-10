import unittest
from flask import Flask
from flask_testing import TestCase
from app import app

class InfectionTreatmentDrugsTests(TestCase):
    """Class for testing the infection treatment drugs section."""

    def create_app(self):
        """Create and configure a new app instance for each test."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_infection_treatment_drugs_section(self):
        """Test the infection treatment drugs section."""
        response = self.client.get('/dashboard/home/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Infection treatment drug as % of all infection treatments', response.data)
        self.assertIn(b'Antibacterials', response.data)
        self.assertIn(b'Antifungal', response.data)
        self.assertIn(b'Antiviral', response.data)
        self.assertIn(b'Antiprotozoal', response.data)
        self.assertIn(b'Anthelmintics', response.data)
        self.assertRegex(response.data.decode('utf-8'), r'\d+%')

if __name__ == "__main__":
    unittest.main()