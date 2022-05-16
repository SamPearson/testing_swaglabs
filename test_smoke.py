from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from engines.swaglabs import SwagLabsEngine
from logs import log_configuration
logger = log_configuration.init_logger(__name__)


class TestSmoke:
    def setup_method(self):
        logger.debug("Initializing a new webdriver")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)

    def test_login(self):
        swag_labs = SwagLabsEngine(self.driver)

        swag_labs.login()
        assert swag_labs.logged_in(), "Cannot confirm the user is logged in and storefront loaded"

    def teardown_method(self):
        logger.debug("Tearing down the old webdriver")
        self.driver.quit()
