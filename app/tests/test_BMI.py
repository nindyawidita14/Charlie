import unittest
from flask import Flask
from flask_testing import TestCase
from app import app

class BMICalculatorTests(TestCase):
    """Class for testing the BMI calculator section."""

    def create_app(self):
        """Create and configure a new app instance for each test."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_bmi_calculator_section(self):
        """Test the BMI calculator section."""
        response = self.client.get('/dashboard/home/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'BMI Calculator For Adult Patient', response.data)
        self.assertIn(b'Weight of patient (kg):', response.data)
        self.assertIn(b'Height of patient (cm):', response.data)
        self.assertIn(b'Calculate', response.data)
        self.assertIn(b'For most adults the BMI below 18.5 is underweight range, 18.5 to 24.9 is healthy weight range, 25 to 29.9 is overweight range, 30 to 39.9 is obese range, 40 or above is severely obese range.', response.data)

if __name__ == "__main__":
    unittest.main()