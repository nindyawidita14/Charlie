import unittest
from flask import Flask
from flask_testing import TestCase
from app import app

class ViewsTests(TestCase):
    """Class for testing views and templates."""

    def create_app(self):
        """Create and configure a new app instance for each test."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_dashboard_home(self):
        """Test the dashboard home page."""
        response = self.client.get('/dashboard/home/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Total number of prescribed antibiotics for each GP practice in a selected PCT', response.data)
        self.assertIn(b'<select class="custom-select" id="input-group-select-2" name="pct-option">', response.data)

    def test_form_submission(self):
        """Test form submission and chart update."""
        response = self.client.post('/dashboard/home/', data={
            'form-id': 'form2',
            'pct-option': '01C'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'chart2', response.data)
        self.assertIn(b'data-labels', response.data)
        self.assertIn(b'data-data', response.data)

if __name__ == "__main__":
    unittest.main()