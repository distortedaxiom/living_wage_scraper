from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()

class StateFetcher:

    def state_list(self):

        url = "https://livingwage.mit.edu/"
        driver.get(url)


if __name__ == "__main__":
    query_request = StateFetcher()
    query_request.state_list()
    input("Press enter to close")