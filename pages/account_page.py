# coding=utf-8
from selenium.webdriver.common.by import By
from pages.base import BasePage
from utils.utils import *
from random import randint
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.restaurant_settings_page import RestaurantSettingsPage
from pages.reservation_popup_page import ReservationPopupPage
from pages.seatIn_page import SeatInPage
import datetime

class AccountPage(BasePage):
    _title = "Account Page"

    _settings_icon = (By.XPATH, "//li[2]/a/i")
    _settings_option = (By.XPATH, "//li[2]/ul/li[2]/a")
    _daily_settings_option = (By.XPATH, "//li[2]/ul/li/a")
    _test_option = (By.XPATH, "//li[2]/ul/li[3]/a")
    _test_shift_name_field = (By.XPATH, "//div/input")
    _test_date_field = (By.XPATH, "//div[2]/input")
    _test_tomorrow_date = str(datetime.date.today().day+1)+"."+str(datetime.date.today().month)+"."+str(datetime.date.today().year)
    _book_now_button = (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div/div/div/button")
    _restaurants_dropdown = (By.XPATH, "//div/span[2]")
    _third_restaurant_option = (By.XPATH, "//div/ul/li[3]")
    _fourth_restaurant_option = (By.XPATH, "//div/ul/li[4]")
    _shifts_menu = (By.XPATH, "//div[2]/div[3]")
    _expand_first_shift_button = (By.XPATH, "//th/span/i")
    _click_first_shift_button = (By.XPATH, "//span[2]/span")
    _first_shift_first_room_name_field = (By.XPATH, "//tr[2]/th/span")
    _first_shift_second_room_name_field = (By.XPATH, "//tr[3]/th/span")
    _seatIn_menu = (By.XPATH, "//li/a")
    _fifth_restaurant_option = (By.XPATH, "//div/ul/li[5]")
    _restaurant_AUTOTESTadhoiofg_option = (By.ID, "zyZJu2ZrYiSXugxsW")
    _restaurant_AUTOTESTaooeigwc_option = (By.ID, "k3bXbWeqHumnqjh73")
    _restaurant_AUTOTESTayruflyu_option = (By.ID, "5xB4k4cGJZx4iXjnF")
    _einloggen_text_field = (By.XPATH, "//h1")

    def __init__(self, driver):
        super(AccountPage, self).__init__(driver, self._title)

    def open_third_restaurant(self):
        self.click(self._restaurants_dropdown)
        self.click(self._third_restaurant_option)

    def open_restaurant_settings(self):
        self.click(self._settings_icon)
        self.click(self._settings_option)
        return RestaurantSettingsPage(self.get_driver())

    def open_fourth_restaurant(self):
        self.click(self._restaurants_dropdown)
        self.click(self._fourth_restaurant_option)

    def open_shifts_menu(self):
        self.click(self._shifts_menu)

    def expand_first_shift(self):
        self.click(self._expand_first_shift_button)

    def click_first_shift(self):
        self.click(self._click_first_shift_button)

    def open_test_page(self):
        self.click(self._settings_icon)
        self.click(self._test_option)

    def fill_in_shift_name_and_tomorrow_date(self, shift_name):
        self.clear_field_and_send_keys(shift_name, self._test_shift_name_field)
        self.clear_field_and_send_keys(self._test_tomorrow_date, self._test_date_field)

    def open_book_now_pupup(self):
        self.click(self._book_now_button)
        return ReservationPopupPage(self.get_driver())

    def open_seatIn(self):
        self.click(self._seatIn_menu)
        return SeatInPage(self.get_driver())

    def open_fifth_restaurant(self):
        self.click(self._restaurants_dropdown)
        self.click(self._fifth_restaurant_option)

    def open_daily_settings(self):
        self.click(self._settings_icon)
        self.click(self._daily_settings_option)
        return RestaurantSettingsPage(self.get_driver())

    def open_AUTOTESTadhoiofg_restaurant(self):
        self.click(self._restaurants_dropdown)
        self.click(self._restaurant_AUTOTESTadhoiofg_option)

    def open_AUTOTESTaooeigwc_restaurant(self):
        self.click(self._restaurants_dropdown)
        self.click(self._restaurant_AUTOTESTaooeigwc_option)

    def open_AUTOTESTayruflyu_restaurant(self):
        self.click(self._restaurants_dropdown)
        self.click(self._restaurant_AUTOTESTayruflyu_option)