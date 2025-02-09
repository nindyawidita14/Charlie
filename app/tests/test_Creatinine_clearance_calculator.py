import unittest
from flask import Flask
from flask_testing import TestCase
from app import app

class CreatinineClearanceCalculatorTests(TestCase):
    """Class for testing the creatinine clearance calculator section."""

    def create_app(self):
        """Create and configure a new app instance for each test."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_creatinine_clearance_calculator_section(self):
        """Test the creatinine clearance calculator section."""
        response = self.client.get('/dashboard/home/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Creatinine Clearance Calculator', response.data)
        self.assertIn(b'Sex of patient:', response.data)
        self.assertIn(b'Age of patient (years):', response.data)
        self.assertIn(b'Weight of patient (kg):', response.data)
        self.assertIn(b'Serum creatinine (micromol/L):', response.data)
        self.assertIn(b'Calculate', response.data)
        self.assertIn(b'This calculates CrCl according to the Cockcroft-Gault equation, for use in patients with stable renal function to estimate creatinine clearance.', response.data)

if __name__ == "__main__":
    unittest.main()