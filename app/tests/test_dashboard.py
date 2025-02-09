import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardTests(unittest.TestCase):
    """Front End Test Case for Dashboard"""

    def setUp(self):
        """Set up the WebDriver (Chrome)"""
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:5000/dashboard/home/")

    def tearDown(self):
        """Close the browser after test"""
        self.driver.quit()

    def test_dashboard_home_page(self):
        """Test the dashboard home page loads correctly"""
        driver = self.driver
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.h3.mb-0.text-gray-800'))
        )
        title = driver.find_element(By.CSS_SELECTOR, 'h1.h3.mb-0.text-gray-800').text
        self.assertEqual(title, 'Prescribing Dashboard')

    def test_total_items_tile(self):
        """Test the total items tile is displayed correctly"""
        driver = self.driver
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.text-xs.font-weight-bold.text-primary.text-uppercase.mb-1'))
        )
        total_items_text = driver.find_element(By.CSS_SELECTOR, '.text-xs.font-weight-bold.text-primary.text-uppercase.mb-1').text
        self.assertIn('Total items:', total_items_text)

    def test_top_prescribed_item(self):
        """Test the top prescribed item tile is displayed correctly"""
        driver = self.driver
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.text-xs.font-weight-bold.text-primary.text-uppercase.mb-1'))
        )
        top_prescribed_item_text = driver.find_element(By.CSS_SELECTOR, '.text-xs.font-weight-bold.text-primary.text-uppercase.mb-1').text
        self.assertIn('TOP PRESCRIBED ITEM:', top_prescribed_item_text)

    def test_form_submission_and_chart_update(self):
        """Test form submission and chart update"""
        driver = self.driver
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'input-group-select-2'))
        )
        select_element = driver.find_element(By.ID, 'input-group-select-2')
        select_element.send_keys('01C')
        driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'chart2'))
        )
        chart_exists = driver.find_element(By.ID, 'chart2').is_displayed()
        self.assertTrue(chart_exists)

    def test_bmi_calculator(self):
        """Test the BMI calculator"""
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, 'div[onclick="popup.showBMICalcFormPopup();"]').click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'BMI-calc'))
        )
        driver.find_element(By.ID, 'weight1').send_keys('70')
        driver.find_element(By.ID, 'height1').send_keys('170')
        driver.find_element(By.ID, 'ctc-button').click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'BMIresult'))
        )
        bmi_result = driver.find_element(By.ID, 'BMIresult').text
        self.assertIn('The estimated BMI result is:', bmi_result)

    def test_creatinine_clearance_calculator(self):
        """Test the creatinine clearance calculator"""
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, 'div[onclick="popup.showCeatCalcFormPopup();"]').click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'creat-calc'))
        )
        driver.find_element(By.ID, 'age').send_keys('30')
        driver.find_element(By.ID, 'weight').send_keys('70')
        driver.find_element(By.ID, 'serum-creatinine').send_keys('100')
        driver.find_element(By.ID, 'sex').send_keys('Male')
        driver.find_element(By.ID, 'ctc-button').click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'result'))
        )
        creatinine_result = driver.find_element(By.ID, 'result').text
        self.assertIn('The estimated creatinine clearance result is:', creatinine_result)

if __name__ == "__main__":
    unittest.main()