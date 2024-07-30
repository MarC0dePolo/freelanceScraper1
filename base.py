from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import credentials
import time
import paths

class GartentechnikScraper:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get(paths.main_page_admin)
        self.currentLink  = ""
        self.filePath = "all_links.txt"
        # Login
        print("Trying to login!")
        self.driver.find_element(By.XPATH, paths.email_xpath).send_keys(credentials.email)
        self.driver.find_element(By.XPATH, paths.pw_xpath).send_keys(credentials.pw)
        self.driver.find_element(By.XPATH, paths.login_button_xpath).click()
        print("Login Successfull")