from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import re

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

    def county_list(self, state):

        list = self.states_list()

        county_list = []
        county_link_holder = []

        for x in list:
            state_link = x[1]
            if state in x[0]:
                driver.get(state_link)

                try:
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "counties"))
                    )

                finally:
                    county_container = driver.find_element_by_class_name('counties')
                    county_container_links = county_container.find_elements_by_css_selector('a')

                    for county in range(len(county_container_links)):
                        county_list.append([county_container_links[county].text])

                    for x in county_container_links:
                        county_link_holder.append(x.get_attribute('href'))

                    for i in range(len(county_list)):
                        county_list[i].append(county_link_holder[i])

                    return county_list

    def county_data(self, state):

        list = self.county_list(state)
        final_list = []
        list_holder = []

        for x in range(0, len(list)):
            driver.get(list[x][1])

            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "results_table"))
                )

            finally:
                data_container = driver.find_elements_by_css_selector('tbody')
                for i in range(len(list)):
                    data_container_body = (data_container[0].text).replace(" ", ",").replace("\n", ',')
                    data_container_body_array = [data_container_body]
                    data_container_body_array.insert(0, list[i][0])
                    data_array = (data_container_body_array[1].split(','))
                    data_array.insert(0, list[x][0])
                    data_array.insert(1, state)
                    filtered_wage_array = [e for e in data_array if e not in ('Living', 'Wage', 'Poverty', 'Minimum')]

                    expenses_container_body = (data_container[1].text.replace(" ", "/").replace("\n", ','))
                    expenses_container_body_array = [expenses_container_body]
                    expenses_array = (expenses_container_body_array[0].split('/'))
                    filtered_expenses_array = [e for e in expenses_array if e not in ('Food', 'Child', 'Care', 'annual', 'income', 'after', 'before', 'taxes')]
                    for i in range(len(filtered_expenses_array)):
                        filtered = re.sub('[^0-9]','', filtered_expenses_array[i])
                        filtered_expenses_array[i] = filtered

                filtered_wage_array.extend(filtered_expenses_array)
                print(filtered_wage_array)
                final_list.append(filtered_wage_array)

        return final_list


if __name__ == "__main__":
    query_request = StateFetcher()
    query_request.county_data("Ohio")
    input("Press enter to close")