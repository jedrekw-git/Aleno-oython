# coding=utf-8
from selenium.webdriver.common.by import By
from pages.base import BasePage
from utils.utils import *
from random import randint
from time import sleep
from unittestzero import Assert
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from pages.restaurant_settings_page import RestaurantSettingsPage
from pages.reservation_popup_page import ReservationPopupPage
from pages.seatIn_page import SeatInPage
from pages.relatin_page import RelatInPage
import datetime

class AccountPage(BasePage):
    _title = "Account Page"

    _settings_icon = (By.CSS_SELECTOR, "i.aleno-icon-setting")
    _settings_option = (By.LINK_TEXT, "Grundeinstellungen")
    _settings_option2 = (By.LINK_TEXT, "Settings")
    _daily_settings_option = (By.LINK_TEXT, "Tageseinstellungen")
    _test_option = (By.NAME, "Test")
    _test_shift_name_field = (By.XPATH, "//div/input")
    _test_date_field = (By.XPATH, "//div[2]/input")
    _test_tomorrow_date = str(datetime.date.today().day+1)+"."+str(datetime.date.today().month)+"."+str(datetime.date.today().year)
    _book_now_button = (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div/div/div/button")
    _restaurants_dropdown = (By.XPATH, "//a/span")
    _shifts_menu = (By.CSS_SELECTOR, "div.toolbar-top-item.toolbar-top-item-shift")
    _expand_first_shift_button = (By.XPATH, "//th/span/i")
    _click_first_shift_button = (By.CSS_SELECTOR, "span.js-go.shift-info > span")
    _first_shift_start_time_field = (By.XPATH, "//span[2]/span[2]/span")
    _first_shift_first_room_name_field = (By.XPATH, "//tr[2]/th/span")
    _first_shift_second_room_name_field = (By.XPATH, "//tr[3]/th/span")
    _seatIn_menu = (By.PARTIAL_LINK_TEXT, "seatIn")
    _einloggen_text_field = (By.XPATH, "//h1")
    _relatin_menu = (By.XPATH, "//li[4]/a")
    _add_notes_button = (By.CSS_SELECTOR, "i.aleno-icon-pen.js-header-calendar-edit-mode-activator")
    _add_note_for_staff_button = (By.XPATH, "//div[2]/a")
    _add_note_for_guests_button = (By.XPATH, "//div/div/div/a")
    _add_note_open_field = (By.XPATH, "//form/div/div[2]/div/div/div")
    _add_note_text_field = (By.XPATH, "//div[3]/div[3]")
    _add_note_text_value = get_random_string(7)+" "+get_random_string(5)
    _add_note_close_field = (By.XPATH, "//form/div/div[2]/div/div/button")
    _add_note_submit_button = (By.XPATH, "//div[2]/button")
    _added_note_type_field = (By.XPATH, "//strong")
    _added_note_type_guests_value = "info für Gäste"
    _added_note_type_staff_value = "info für Personal"
    _added_note_value_field = (By.XPATH, "//div[3]/div/div[2]/div/div/span")
    _remove_added_note_button = (By.XPATH, "//div[4]/i")
    _remove_added_note_submit_yes_button = (By.XPATH, "//div[2]/div/button")

    def __init__(self, driver):
        super(AccountPage, self).__init__(driver, self._title)

    def open_restaurant_settings(self):
        self.click(self._settings_icon, "Settings icon cannot be clicked or wasn't found on the page")
        try:
            self.click(self._settings_option, "Settings option on the dropdown cannot be clicked or wasn't found on the page")
        except TimeoutException:
            self.click(self._settings_option2, "Settings option on the dropdown cannot be clicked or wasn't found on the page")
        # if WebDriverWait.until(EC.element_to_be_clickable, self._settings_option):
        #
        # else:
        #     self.click(self._settings_option2)
        return RestaurantSettingsPage(self.get_driver())

    def open_shifts_menu(self):
        try:
            self.click(self._shifts_menu, "The shifts menu on the dashboard cannot be clicked or wasn't found on the page")
        except WebDriverException as e:
            self.get_driver().execute_script("arguments[0].click();", self.find_element(self._shifts_menu))
        sleep(3)

    def expand_first_shift(self):
        try:
            self.click(self._expand_first_shift_button, "The expand first shift button cannot be clicked or wasn't found on the shifts menu page")
        except WebDriverException as e:
            self.get_driver().execute_script("arguments[0].click();", self.find_element(self._expand_first_shift_button))

    def click_first_shift(self):
        try:
            self.click(self._click_first_shift_button, "The first shift button cannot be clicked or isn't present on the shifts menu page")
        except WebDriverException as e:
            self.get_driver().execute_script("arguments[0].click();", self.find_element(self._click_first_shift_button))
        return SeatInPage(self.get_driver())

    def get_first_shift_start_time(self):
        self.first_shift_start_time = self.get_text(self._first_shift_start_time_field)

    def open_test_page(self):
        self.click(self._settings_icon, "The settings icon couldn't be clicked or wasn't found on the dashboard page")
        self.click(self._test_option, "The test option on the settings dropdown couldn't be clicked or wasn't found on dashboard page")

    def fill_in_shift_name_and_tomorrow_date(self, shift_name):
        self.clear_field_and_send_keys(shift_name, self._test_shift_name_field)
        self.clear_field_and_send_keys(self._test_tomorrow_date, self._test_date_field)

    def open_book_now_pupup(self):
        self.click(self._book_now_button, "The button to open book now popup couldn't be clicked or wasn't found on the test-popup page")
        return ReservationPopupPage(self.get_driver())

    def open_seatIn(self):
        self.click(self._seatIn_menu, "The button to open SeatIn menu cannot be clicked or wasn't found on the dashboard")
        return SeatInPage(self.get_driver())

    def open_daily_settings(self):
        try:
            self.click(self._settings_icon, "The settings icon cannot be clicked or wasn't found on the dashboard")
        except WebDriverException as e:
            self.get_driver().execute_script("arguments[0].click();", self.find_element(self._settings_icon))
        self.click(self._daily_settings_option, "The daily settings option in the settings dropdown cannot be clicked or wasn't found in the dropdown")
        return RestaurantSettingsPage(self.get_driver())

    def open_relatIn(self):
        self.click(self._relatin_menu, "The button to open relatIn cannot be clicked or wasn't found on the dashboard")
        return RelatInPage(self.get_driver())

    def add_note_for_staff(self):
        self.click(self._add_notes_button, "The add note button cannot be clicked or wasn't found on the shifts menu page")
        self.click(self._add_note_for_staff_button, "The add note for staff button cannot be clicked or wasn't found on the shifts menu page")
        sleep(2)
        self.click(self._add_note_open_field, "The attempt to open add note text field to enter data to it wasn't successful")
        self.click(self._add_note_text_field, "The attempt to click add note text field to enter data to it wasn't successful")
        self.clear_field_and_send_keys(self._add_note_text_value, self._add_note_text_field)
        self.click(self._add_note_close_field, "The attempt to close add note text field after entering data to it wasn't successful")
        self.click(self._add_note_submit_button, "The attempt to click add note submit button wasn't successful")
        sleep(2)

    def add_note_for_guests(self):
        self.click(self._add_notes_button, "The add note button cannot be clicked or wasn't found on the shifts menu page")
        # WebDriverWait(self.get_driver(), 15).until(EC.element_to_be_clickable(self._add_note_for_guests_button))
        self.click(self._add_note_for_guests_button, "The add note for guests button cannot be clicked or wasn't found on the shifts menu page")
        sleep(2)
        self.click(self._add_note_open_field, "The attempt to open add note text field to enter data to it wasn't successful")
        self.click(self._add_note_text_field, "The attempt to click add note text field to enter data to it wasn't successful")
        self.clear_field_and_send_keys(self._add_note_text_value, self._add_note_text_field)
        self.click(self._add_note_close_field, "The attempt to close add note text field after entering data to it wasn't successful")
        self.click(self._add_note_submit_button, "The attempt to click add note submit button wasn't successful")
        sleep(2)

    def click_add_notes_button(self):
        self.click(self._add_notes_button, "The add note button cannot be clicked or wasn't found on the shifts menu page")

    def remove_added_note(self):
        self.click(self._add_notes_button, "The add note button cannot be clicked or wasn't found on the shifts menu page")
        self.click(self._remove_added_note_button, "The remove note button cannot be clicked or wasn't found on the shifts menu page")
        self.click(self._remove_added_note_submit_yes_button, "The add note  submit \"yes\" button cannot be clicked or wasn't found on the shifts menu page")
        self.click(self._add_notes_button, "The add note button cannot be clicked or wasn't found on the shifts menu page")

    def get_text_added_note_type(self):
        self.added_note_type_text = (self.get_text(self._added_note_type_field)).encode('utf-8')

    def open_registered_restaurant(self, restaurant_name):
        self.click(self._restaurants_dropdown, "Dropdown of chosing restaurant wasn't found on the page")
        try:
            self.click((By.NAME, "%s" %restaurant_name), "Restaurant name wasn't found on the chosing restaurant dropdown")
        except WebDriverException as e:
            self.get_driver().execute_script("arguments[0].click();", self.find_element((By.NAME, "%s" %restaurant_name)))
