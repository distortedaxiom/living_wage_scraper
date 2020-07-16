from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()

class StateFetcher:

    def state_list(self):

        states_list = []

        url = "https://livingwage.mit.edu/"
        driver.get(url)

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "states"))
            )

        finally:
            state_container = driver.find_element_by_class_name('states')
            state_container_links = state_container.find_elements_by_css_selector('a')

        for state in range(len(state_container_links)):
            states_list.append([state_container_links[state].text])

        print(states_list)

        for x in state_container_links:
            print(x.get_attribute('href'))



if __name__ == "__main__":
    query_request = StateFetcher()
    query_request.state_list()
    input("Press enter to close")