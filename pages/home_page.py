from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    CHECK_IN = (By.XPATH, "(//div[contains(@class,'dateWrapper')]//input)[1]")
    CHECK_OUT = (By.XPATH, "(//div[contains(@class,'dateWrapper')]//input)[2]")
    CHECK_AVAILABILITY_BTN = (By.XPATH, "//button[text()='Check Availability']")

    def open(self, url):
        self.driver.get(url)

    def select_dates(self, check_in, check_out):
        check_in_field = self.driver.find_element(*self.CHECK_IN)
        check_out_field = self.driver.find_element(*self.CHECK_OUT)

        check_in_field.click()
        self.driver.execute_script(
            "arguments[0].value = arguments[1]", check_in_field, check_in
        )

        check_out_field.click()
        self.driver.execute_script(
            "arguments[0].value = arguments[1]", check_out_field, check_out
        )

    def click_check_availability(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECK_AVAILABILITY_BTN)
        ).click()

    def wait_for_check_in(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.CHECK_IN)
        )