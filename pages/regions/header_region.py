# coding=utf-8
from selenium.webdriver.common.by import By
from pages.page import Page
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.register_restaurant_page import RegisterRestaurantPage
from pages.account_page import AccountPage

class HeaderRegion(Page):
    _login_field = (By.NAME, "email")
    _password_field = (By.NAME, "password")
    _login_submit = (By.XPATH, "//div[3]/div/button")
    _base_url = "http://test.aleno.me/"
    _base_url2 = "http://stg.aleno.me/"
    _aleno_logo = (By.XPATH, "//img")


    def login(self, login, password):
        self.clear_field_and_send_keys(login, self._login_field)
        self.clear_field_and_send_keys(password, self._password_field)
        self.click(self._login_submit)
        return AccountPage(self.get_driver())

    def open_register_restaurant_page(self):
        self.get(self._base_url + "restaurants/new")
        return RegisterRestaurantPage(self.get_driver())

    def logout(self):
        self.get(self._base_url + "logout")

    def open_account_page(self):
        self.get(self._base_url)
        return AccountPage(self.get_driver())
