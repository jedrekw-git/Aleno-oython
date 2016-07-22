# coding=utf-8
from selenium.webdriver.common.by import By
from pages.base import BasePage
from utils.utils import *
from random import randint
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class RelatInPage(BasePage):
    _title = "RelatIn Page"

    _add_client_button = (By.XPATH, "//div[2]/div/div/div/div/button")
    _client_first_name_field = (By.NAME, "firstName")
    _client_first_name_value = get_random_string(6)
    _client_last_name_field = (By.NAME, "lastName")
    _client_last_name_value = get_random_string(8)
    _client_phone_number_field = (By.NAME, "phoneNumber")
    _client_phone_number_value = get_random_integer(7)
    _client_email_field = (By.NAME, "primaryEmail")
    _client_email_value = get_random_string(7)+"@"+get_random_string(5)+".pl"
    _client_description_field = (By.NAME, "description")
    _client_description_value = get_random_string(4)+" "+get_random_string(5)+" "+get_random_string(7)
    _client_category_field = (By.NAME, "category")
    _client_category_value = get_random_string(6)
    _save_client_button = (By.XPATH, "//div[2]/button")
    _added_client_first_name_field = (By.XPATH, "//td/a")
    _added_client_last_name_field = (By.XPATH, "//td[2]/a")
    _added_client_phone_number_field = (By.XPATH, "//td[3]/a")
    _added_client_email_field = (By.XPATH, "//div[2]/div/div/table/tbody/tr/td[4]")
    _added_client_category_field = (By.XPATH, "//div[2]/div/div/table/tbody/tr/td[5]/span")
    _remove_first_client_button = (By.XPATH, '//td[10]/button')

    def __init__(self, driver):
        super(RelatInPage, self).__init__(driver, self._title)

    def add_client(self):
        self.click(self._add_client_button)
        WebDriverWait(self.get_driver(), 15).until(EC.visibility_of_element_located(self._client_first_name_field))
        self.click(self._client_first_name_field)
        self.clear_field_and_send_keys(self._client_first_name_value, self._client_first_name_field)
        self.clear_field_and_send_keys(self._client_last_name_value, self._client_last_name_field)
        self.clear_field_and_send_keys(self._client_phone_number_value, self._client_phone_number_field)
        self.clear_field_and_send_keys(self._client_email_value, self._client_email_field)
        self.clear_field_and_send_keys(self._client_description_value, self._client_description_field)
        self.clear_field_and_send_keys(self._client_category_value, self._client_category_field)
        self.click(self._save_client_button)

    def remove_first_client(self):
        try:
            self.click(self._remove_first_client_button)
        except WebDriverException as e:
            self.get_driver().execute_script("arguments[0].click();", self.find_element(self._remove_first_client_button))
        self.accept_alert()








