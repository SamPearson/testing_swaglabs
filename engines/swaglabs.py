from selenium.webdriver.common.by import By
from logs import log_configuration
logger = log_configuration.init_logger(__name__)


class SwagLabsEngine():
    def __init__(self, driver):
        self.driver = driver

    def login(self, username="standard_user", password="secret_sauce"):
        self.driver.get("https://www.saucedemo.com/")

        user_field = self.driver.find_element(By.XPATH, "//input[@data-test='username']")
        user_field.send_keys(username)

        password_field = self.driver.find_element(By.XPATH, "//input[@data-test='password']")
        password_field.send_keys(password)

        logger.debug("Ready to click the login button")
        login_button = self.driver.find_element(By.XPATH, "//input[@data-test='login-button']")
        login_button.click()

    def logged_in(self):
        if len(self.driver.find_elements(By.XPATH, "//a[@class='shopping_cart_link']")) <= 0:
            print("did not find shopping cart link")
            return False

        if len(self.driver.find_elements(By.XPATH, "//button[@id='react-burger-menu-btn']")) <= 0:
            print("did not find hambutton")
            return False

        return True
