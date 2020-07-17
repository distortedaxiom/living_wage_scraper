from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()

class StateFetcher:

    def states_list(self):

        states_list = []
        states_link_holder = []

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

        for x in state_container_links:
            states_link_holder.append(x.get_attribute('href'))

        for i in range(len(states_list)):
            states_list[i].append(states_link_holder[i])

        return states_list

    def county_finder(self):

        list = self.states_list()
        print(list)





if __name__ == "__main__":
    query_request = StateFetcher()
    query_request.county_finder()
    input("Press enter to close")