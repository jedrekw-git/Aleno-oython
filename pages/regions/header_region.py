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
    _base_url2 = "http://test.aleno.me/"
    _base_url = "http://stg.aleno.me/"
    _aleno_logo = (By.XPATH, "//img")
    _einloggen_text = (By.XPATH, "//h1")

    def login(self, login, password):
        self.clear_field_and_send_keys(login, self._login_field, "The login field wasn't found on login page")
        self.clear_field_and_send_keys(password, self._password_field, "The password field wasn't found on login page")
        self.click(self._login_submit, "Button to submit login action wasn't found on the login page")
        return AccountPage(self.get_driver())

    def open_register_restaurant_page(self):
        self.get(self._base_url + "restaurants/new")
        return RegisterRestaurantPage(self.get_driver())

    def logout(self):
        self.get(self._base_url + "logout")

    def open_account_page(self):
        self.get(self._base_url)
        return AccountPage(self.get_driver())

    def click_account_page(self):
        self.click(self._aleno_logo, "Aleno logo wasn't found")
        return AccountPage(self.get_driver())
