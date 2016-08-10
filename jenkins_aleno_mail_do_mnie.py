# coding=utf-8
import unittest
from selenium import webdriver
from htmltestrunner import HTMLTestRunner
from unittestzero import Assert
from pages.home import HomePage
from utils.config import *
from utils.utils import *
from time import sleep
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.remote.webelement import *
from time import gmtime, strftime
import re
from selenium.webdriver.remote.webelement import *
from selenium.webdriver.common.action_chains import *
import datetime as dt
from datetime import datetime
from selenium.common.exceptions import *

SCREEN_DUMP_LOCATION = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'screendumps'
)
run_locally = True

# @on_platforms(browsers)


class SmokeTest(unittest.TestCase):
    _internal_non_grouped_domain_text = 1

    def test_aa_prepare_test_environment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(home_page.header._einloggen_text, "Einloggen"),"\"Einloggen\" text wasn't found on the login page")
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        if not "AUTOTESTa" in home_page.header.get_page_source():
            register_restaurant_page = home_page.header.open_register_restaurant_page()
            register_restaurant_page.enter_restaurant_data("AUTOTESTa")
            account_page = register_restaurant_page.save_restaurant()
            home_page.header.click_account_page()
            account_page.open_registered_restaurant("AUTOTESTa")
        if not "AUTOTESTb" in home_page.header.get_page_source():
            register_restaurant_page = home_page.header.open_register_restaurant_page()
            register_restaurant_page.enter_restaurant_data("AUTOTESTb")
            account_page = register_restaurant_page.save_restaurant()
            home_page.header.click_account_page()
            account_page.open_registered_restaurant("AUTOTESTb")
            restaurant_settings_page = account_page.open_restaurant_settings()
            restaurant_settings_page.open_rooms_tab()
            restaurant_settings_page.add_two_rooms()

    def test_login_and_logout_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(home_page.header._einloggen_text, "Einloggen"),"\"Einloggen\" text wasn't found on the login page")
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        home_page.header.logout()
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(home_page.header._einloggen_text, "Einloggen"),"\"Einloggen\" text wasn't found on the login page")

    def test_register_restaurant_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(home_page.header._einloggen_text, "Einloggen"),"\"Einloggen\" text wasn't found on the login page")
        home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            home_page.header.login(USER, PASSWORD)
        register_restaurant_page = home_page.header.open_register_restaurant_page()
        register_restaurant_page.enter_restaurant_data(register_restaurant_page._last_name_value)
        account_page = register_restaurant_page.save_restaurant()
        home_page.header.click_account_page()
        account_page.open_registered_restaurant(register_restaurant_page._last_name_value)
        sleep(6)
        restaurant_settings_page = account_page.open_restaurant_settings()
        restaurant_settings_page.get_restaurant_info()

        Assert.equal(restaurant_settings_page.restaurant_info_last_name, register_restaurant_page._last_name_value, "Restaurant name on the settings page isn't equal to the restaurant name entered during the registration restaurant process")
        Assert.equal(restaurant_settings_page.restaurant_info_address, register_restaurant_page._address_value, "Restaurant address value on the settings page isn't equal to the restaurant address value entered during the registration restaurant process")
        Assert.equal(restaurant_settings_page.restaurant_info_zip, register_restaurant_page._zip_code_value, "Restaurant zip code value on the settings page isn't equal to the restaurant zip code entered during the registration restaurant process")
        Assert.equal(restaurant_settings_page.restaurant_info_city, register_restaurant_page._city_value, "Restaurant city value on the settings page isn't equal to the restaurant city value entered during the registration restaurant process")
        Assert.equal(restaurant_settings_page.restaurant_info_country, register_restaurant_page._country_value, "Restaurant country value on the settings page isn't equal to the restaurant country value entered during the registration restaurant process")
        Assert.equal(restaurant_settings_page.restaurant_info_email, register_restaurant_page._email_value, "Restaurant email value on the settings page isn't equal to the restaurant email value entered during the registration restaurant process")
        Assert.equal(restaurant_settings_page.restaurant_info_senders_email, register_restaurant_page._senders_email_value, "Restaurant senders email value on the settings page isn't equal to the restaurant senders email value entered during the registration restaurant process")
        Assert.equal(restaurant_settings_page.restaurant_info_msgIn_email, register_restaurant_page._msgIn_email_value, "Restaurant magIn email value on the settings page isn't equal to the restaurant magIn email value entered during the registration restaurant process")
        Assert.equal(restaurant_settings_page.restaurant_info_website, register_restaurant_page._website_value, "Restaurant website address on the settings page isn't equal to the restaurant website address entered during the registration restaurant process")
        Assert.equal(restaurant_settings_page.restaurant_info_facebook, register_restaurant_page._facebook_value, "Restaurant facebook address on the settings page isn't equal to the restaurant facebook address entered during the registration restaurant process")
        Assert.equal(restaurant_settings_page.restaurant_info_fan_page, register_restaurant_page._fan_page_url_value, "Restaurant fan page url on the settings page isn't equal to the restaurant fan page url entered during the registration restaurant process")
        Assert.equal(restaurant_settings_page.restaurant_info_trip_advisor, register_restaurant_page._trip_advisor_value, "Restaurant trip advisor on the settings page isn't equal to the restaurant trip advisor entered during the registration restaurant process")
        Assert.equal(restaurant_settings_page.restaurant_info_google, register_restaurant_page._google_value, "Restaurant google address on the settings page isn't equal to the restaurant google address entered during the registration restaurant process")
        Assert.equal(restaurant_settings_page.restaurant_info_yelp, register_restaurant_page._yelp_value, "Restaurant yelp on the settings page isn't equal to the restaurant yelp entered during the registration restaurant process")
        Assert.equal(restaurant_settings_page.restaurant_info_phone, register_restaurant_page._phone_value, "Restaurant phone value on the settings page isn't equal to the restaurant phone value entered during the registration restaurant process")
        Assert.equal(restaurant_settings_page.restaurant_info_image_url, register_restaurant_page._image_url_value, "Restaurant image url on the settings page isn't equal to the restaurant image url entered during the registration restaurant process")

#random language do sprawdzenia

    def test_add_rooms_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(home_page.header._einloggen_text, "Einloggen"),"\"Einloggen\" text wasn't found on the login page")
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_registered_restaurant("AUTOTESTa")
        restaurant_settings_page = account_page.open_restaurant_settings()
        restaurant_settings_page.open_rooms_tab()
        restaurant_settings_page.add_two_rooms()
        restaurant_settings_page.remove_added_rooms()

        self.not_contains(restaurant_settings_page._add_room_name_value1, restaurant_settings_page.get_page_source(), "Added room name value was found in the website source code, although it shouldn't be because it should be deleted")
        self.not_contains(restaurant_settings_page._add_room_name_value2, restaurant_settings_page.get_page_source(), "Added room name value was found in the website source code, although it shouldn't be because it should be deleted")

    def test_add_shift_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(home_page.header._einloggen_text, "Einloggen"),"\"Einloggen\" text wasn't found on the login page")
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_registered_restaurant("AUTOTESTa")
        restaurant_settings_page = account_page.open_restaurant_settings()
        restaurant_settings_page.open_shift_tab()
        while True:
            if restaurant_settings_page._shift_name_value in account_page.get_page_source():
                restaurant_settings_page.remove_first_shift()
            if not restaurant_settings_page._shift_name_value in account_page.get_page_source():
                break
        restaurant_settings_page.add_shift_first_accordeon()
        restaurant_settings_page.add_shift_second_accordeon()
        restaurant_settings_page.save_shift()
        restaurant_settings_page.open_first_shift_details()
        restaurant_settings_page.first_shift_get_values()

        Assert.equal(restaurant_settings_page.added_shift_name, restaurant_settings_page._shift_name_value, "Shift name on the first shift show copies page isn't equal to shift name entered in the adding shift form")
        Assert.equal(restaurant_settings_page.added_shift_internal_name, restaurant_settings_page._shift_internal_name_value, "Shift internal name on the first shift show copies page isn't equal to shift internal name entered in the adding shift form")
        # Assert.equal(restaurant_settings_page.added_shift_capacity, restaurant_settings_page._shift_capacity_value, "Shift capacity on the first shift show copies page isn't equal to shift capacity entered in the adding shift form")
        Assert.equal(restaurant_settings_page.added_shift_buffer, restaurant_settings_page._shift_buffer_value, "Shift buffer on the first shift show copies page isn't equal to shift buffer entered in the adding shift form")
        Assert.equal(restaurant_settings_page.added_shift_daily_deadlinie, restaurant_settings_page._shift_daily_online_deadline_value, "Shift daily online deadline on the first shift show copies page isn't equal to shift daily online deadline entered in the adding shift form")
        Assert.equal(restaurant_settings_page.added_shift_kitchen_start, restaurant_settings_page._shift_kitchen_start_value, "Shift kitchen start on the first shift show copies page isn't equal to shift kitchen start entered in the adding shift form")
        Assert.equal(restaurant_settings_page.added_shift_kitchen_end, restaurant_settings_page._shift_kitchen_end_value, "Shift kitchen end on the first shift show copies page isn't equal to shift kitchen end entered in the adding shift form")
        Assert.equal(restaurant_settings_page.added_shift_timeslot_capacity, restaurant_settings_page._shift_timeslot_capacity_value, "Shift timeslot capacity on the first shift show copies page isn't equal to shift timeslot capacity entered in the adding shift form")
        Assert.equal(restaurant_settings_page.added_shift_reservations_confirmed, restaurant_settings_page._shift_reservations_confirmed_value, "Shift reservation confirmed on the first shift show copies page isn't equal to shift reservation confirmed entered in the adding shift form")
        Assert.equal(restaurant_settings_page.added_shift_minimum_guests, restaurant_settings_page._shift_minimum_guests_value, "Shift minimum guests value on the first shift show copies page isn't equal to shift minimum guests value entered in the adding shift form")
        Assert.equal(restaurant_settings_page.added_shift_maximum_guests, restaurant_settings_page._shift_maximum_guests_value, "Shift maximum guests value on the first shift show copies page isn't equal to shift maximum guests value entered in the adding shift form")

        restaurant_settings_page = account_page.open_restaurant_settings()
        restaurant_settings_page.open_shift_tab()
        restaurant_settings_page.remove_first_shift()

        self.not_contains(restaurant_settings_page._shift_name_value, restaurant_settings_page.get_page_source(), "Added restaurant shift name was found on the restaurant shifts settings page, although it shouldn't be because the shift should be removed")
        self.not_contains(restaurant_settings_page._shift_internal_name_value, restaurant_settings_page.get_page_source(), "Added restaurant shift internal name was found on the restaurant shifts settings page, although it shouldn't be because the shift should be removed")

    def test_archive_shift_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(home_page.header._einloggen_text, "Einloggen"),"\"Einloggen\" text wasn't found on the login page")
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_registered_restaurant("George Bar & Grill")
        restaurant_settings_page = account_page.open_restaurant_settings()
        restaurant_settings_page.open_shift_tab()
        restaurant_settings_page.get_first_shift_internal_name()
        restaurant_settings_page.archive_first_shift()
        sleep(3)

        Assert.not_equal(restaurant_settings_page._first_shift_internal_name, restaurant_settings_page.get_text(restaurant_settings_page._first_shift_internal_name_field), "First shift internal name after action of archive first shift is equal to first shift internal name before action of archive first shift, although it shouldn't be because shift should be moved to archived shifts tab on the restaurant shifts settings page")
        restaurant_settings_page.expand_archived_shifts()
        Assert.equal(restaurant_settings_page._first_shift_internal_name, restaurant_settings_page.get_text(restaurant_settings_page._first_archived_shift_internal_name_field), "First shift internal name before action of archive first shift isn't equal to first shift internal name in the archived shifts tab so probably shoft wasn't moved to archived shifts tab on the restaurant shifts settings page")
        restaurant_settings_page.unachive_shift()

        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(restaurant_settings_page._first_shift_internal_name_field, restaurant_settings_page._first_shift_internal_name), "First shift internal name isn't equal first shift internal name before action of achive and unarchive shift, so probably the shift wasn't unachived on the restaurant shifts settings page")
        Assert.true(self.is_element_present("//table[2]/tbody/tr/td[2]")==False, "Archived shifts tab is present on the page, although it shouldn't be because the shift was unarchived on the restaurant shifts settings page")

    def test_add_room_to_shift_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(home_page.header._einloggen_text, "Einloggen"),"\"Einloggen\" text wasn't found on the login page")
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_registered_restaurant("AUTOTESTb")
        restaurant_settings_page = account_page.open_restaurant_settings()
        restaurant_settings_page.open_shift_tab()
        restaurant_settings_page.add_shift_first_accordeon()
        restaurant_settings_page.add_1_room_to_shift()
        restaurant_settings_page.save_shift()

        account_page = home_page.header.click_account_page()
        account_page.open_shifts_menu()
        account_page.expand_first_shift()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(account_page._first_shift_first_room_name_field, restaurant_settings_page.first_room_name), "First shift first room name value in the shifts menu isn't equal to room name added to shift")

        account_page = home_page.header.click_account_page()
        restaurant_settings_page = account_page.open_restaurant_settings()
        restaurant_settings_page.open_shift_tab()
        restaurant_settings_page.remove_first_shift()

        self.not_contains(restaurant_settings_page._shift_name_value, restaurant_settings_page.get_page_source(), "Added restaurant shift name was found on the restaurant shifts settings page, although it shouldn't be because the shift should be removed")
        self.not_contains(restaurant_settings_page._shift_internal_name_value, restaurant_settings_page.get_page_source(), "Added restaurant shift internal name was found on the restaurant shifts settings page, although it shouldn't be because the shift should be removed")

    def test_add_two_rooms_to_shift_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(home_page.header._einloggen_text, "Einloggen"),"\"Einloggen\" text wasn't found on the login page")
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_registered_restaurant("AUTOTESTb")
        restaurant_settings_page = account_page.open_restaurant_settings()
        restaurant_settings_page.open_shift_tab()
        while True:
            if restaurant_settings_page._shift_name_value in account_page.get_page_source():
                restaurant_settings_page.remove_first_shift()
            if not restaurant_settings_page._shift_name_value in account_page.get_page_source():
                break
        restaurant_settings_page.add_shift_first_accordeon()
        restaurant_settings_page.add_shift_second_accordeon()
        restaurant_settings_page.add_2_rooms_to_shift_publish()
        restaurant_settings_page.save_shift()

        account_page = home_page.header.click_account_page()
        account_page.open_shifts_menu()
        account_page.expand_first_shift()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(account_page._first_shift_first_room_name_field, restaurant_settings_page.first_room_name), "The first shift first room name in the shifts menu isn't equal to first room name added to shift, probably the room wasn't added or is not visible in the right place")
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(account_page._first_shift_second_room_name_field, restaurant_settings_page.second_room_name), "The first shift second room name in the shifts menu isn't equal to second room name added to shift, probably the room wasn't added or is not visible in the right place")

        # account_page = home_page.header.open_account_page()
        # account_page.open_test_page()
        # account_page.fill_in_shift_name_and_tomorrow_date(restaurant_settings_page._shift_name_value)
        # reservation_popup_page = account_page.open_book_now_pupup()
        #
        # sleep(5)
        # reservation_popup_page.click_first_shift()
        #
        # Assert.contains(restaurant_settings_page.first_room_name, reservation_popup_page.get_page_source())
        # Assert.contains(restaurant_settings_page.second_room_name, reservation_popup_page.get_page_source())

        account_page = home_page.header.click_account_page()
        restaurant_settings_page = account_page.open_restaurant_settings()
        restaurant_settings_page.open_shift_tab()
        restaurant_settings_page.remove_first_shift()

        self.not_contains(restaurant_settings_page._shift_name_value, restaurant_settings_page.get_page_source(), "Added restaurant shift name was found on the restaurant shifts settings page, although it shouldn't be because the shift should be removed")
        self.not_contains(restaurant_settings_page._shift_internal_name_value, restaurant_settings_page.get_page_source(), "Added restaurant shift internal name was found on the restaurant shifts settings page, although it shouldn't be because the shift should be removed")

#NIE WIDZI POPUP'U

    def test_add_table_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(home_page.header._einloggen_text, "Einloggen"),"\"Einloggen\" text wasn't found on the login page")
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_registered_restaurant("AUTOTESTa")
        restaurant_settings_page = account_page.open_restaurant_settings()
        restaurant_settings_page.open_tables_tab()
        restaurant_settings_page.add_table()

        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(restaurant_settings_page._first_table_name_field, restaurant_settings_page._table_name_value), "The added table name is not equal to value in first table  - name field in the tables settings tab, probably the table wasn't added or isn't visible in the right place")
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(restaurant_settings_page._first_table_capacity_field, restaurant_settings_page._table_capacity_value), "The added table capacity is not equal to value in first table  - capacity field in the tables settings tab, probably the table wasn't added or isn't visible in the right place")

        restaurant_settings_page.remove_first_table()

        self.not_contains(restaurant_settings_page._table_name_value, restaurant_settings_page.get_page_source(), "Added table name value is found in the tables tab page source, although it shouldn't be because the table should be removed")
        # self.not_contains(restaurant_settings_page._table_capacity_value, restaurant_settings_page.get_page_source(), "Added table capacity value is found in the tables tab page source, although it shouldn't be because the table should be removed")

    def test_add_and_edit_holiday_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(home_page.header._einloggen_text, "Einloggen"),"\"Einloggen\" text wasn't found on the login page")
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_registered_restaurant("AUTOTESTa")
        restaurant_settings_page = account_page.open_restaurant_settings()
        restaurant_settings_page.open_holidays_tab()
        while True:
            try:
                WebDriverWait(self.driver, 7).until(EC.presence_of_element_located(restaurant_settings_page._first_added_holiday_name_field), "The first holiday on the holiday settings page is not visible")
                restaurant_settings_page.remove_added_holiday()
            except WebDriverException as e:
                break

        restaurant_settings_page.add_holiday()

        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(restaurant_settings_page._first_added_holiday_name_field, restaurant_settings_page._holiday_name_value), "The first holiday name on holidays tab isn't equal to holiday name entered while adding holiday, probably the holiday wasn't added or isn't visible in the right place")
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(restaurant_settings_page._first_added_holiday_from_field, restaurant_settings_page._holiday_start_date_value), "The first holiday \"from\" value on holidays tab isn't equal to holiday \"from\" value entered while adding holiday, probably the holiday wasn't added or isn't visible in the right place")
        if (dt.date.today().day)==29 and (dt.date.today().month)==2:
            WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(restaurant_settings_page._first_added_holiday_to_field, restaurant_settings_page._first_day_next_month), "The first holiday \"to\" value on holidays tab isn't equal to holiday \"to\" value entered while adding holiday, probably the holiday wasn't added or isn't visible in the right place")
        elif (dt.date.today().day)==30 or (dt.date.today().day)==31:
            WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(restaurant_settings_page._first_added_holiday_to_field, restaurant_settings_page._first_day_next_month), "The first holiday \"to\" value on holidays tab isn't equal to holiday \"to\" value entered while adding holiday, probably the holiday wasn't added or isn't visible in the right place")
        else:
            WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(restaurant_settings_page._first_added_holiday_to_field, restaurant_settings_page._holiday_end_date_value), "The first holiday \"to\" value on holidays tab isn't equal to holiday \"to\" value entered while adding holiday, probably the holiday wasn't added or isn't visible in the right place")
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(restaurant_settings_page._first_added_holiday_information_field, restaurant_settings_page._holiday_information_value), "The first holiday \"Information\" value on holidays tab isn't equal to holiday \"Information\" value entered while adding holiday, probably the holiday wasn't added or isn't visible in the right place")

        restaurant_settings_page.edit_holiday()

        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(restaurant_settings_page._first_added_holiday_name_field, restaurant_settings_page._edit_holiday_name_value), "The first holiday name on holidays tab isn't equal to holiday name entered while editing holiday, probably the holiday wasn't edited or isn't visible in the right place")
        if (dt.date.today().day)==1:
            WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(restaurant_settings_page._first_added_holiday_from_field, restaurant_settings_page._last_day_previous_month), "The first holiday \"from\" value on holidays tab isn't equal to holiday \"from\" value entered while editing holiday, probably the holiday wasn't edited or isn't visible in the right place")
        else:
            WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(restaurant_settings_page._first_added_holiday_from_field, restaurant_settings_page._edit_holiday_start_date_value), "The first holiday \"from\" value on holidays tab isn't equal to holiday \"from\" value entered while editing holiday, probably the holiday wasn't edited or isn't visible in the right place")
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(restaurant_settings_page._first_added_holiday_to_field, restaurant_settings_page._edit_holiday_end_date_value), "The first holiday \"to\" value on holidays tab isn't equal to holiday \"to\" value entered while editing holiday, probably the holiday wasn't edited or isn't visible in the right place")
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(restaurant_settings_page._first_added_holiday_information_field, restaurant_settings_page._edit_holiday_information_value), "The first holiday \"information\" value on holidays tab isn't equal to holiday \"information\" value entered while editing holiday, probably the holiday wasn't edited or isn't visible in the right place")

        restaurant_settings_page.remove_added_holiday()

        self.not_contains(restaurant_settings_page._edit_holiday_name_value, restaurant_settings_page.get_page_source(), "THe holiday name value was found on the holidays tab, although it shouldn't be because the holiday should be removed")
        if (dt.date.today().day)==1:
            self.not_contains(restaurant_settings_page._last_day_previous_month, restaurant_settings_page.get_page_source(), "THe holiday start date value was found on the holidays tab, although it shouldn't be because the holiday should be removed")
        else:
            self.not_contains(restaurant_settings_page._edit_holiday_start_date_value, restaurant_settings_page.get_page_source(), "THe holiday start date value was found on the holidays tab, although it shouldn't be because the holiday should be removed")
        self.not_contains(restaurant_settings_page._edit_holiday_end_date_value, restaurant_settings_page.get_page_source(), "THe holiday end date value was found on the holidays tab, although it shouldn't be because the holiday should be removed")
        # self.not_contains(restaurant_settings_page._edit_holiday_information_value, restaurant_settings_page.get_page_source(), "THe holiday information value was found on the holidays tab, although it shouldn't be because the holiday should be removed")

#restaurant_settings_page._edit_holiday_information_value remains in page source, zgłoszone

    def test_edit_customizations_tab_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(home_page.header._einloggen_text, "Einloggen"),"\"Einloggen\" text wasn't found on the login page")
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_registered_restaurant("AUTOTESTa")
        restaurant_settings_page = account_page.open_restaurant_settings()
        restaurant_settings_page.open_coustomizations_tab()
        if not self.driver.find_element_by_name("serviceRole80").is_enabled():
            restaurant_settings_page.click_percentage_of_capacity_checkbox()
        restaurant_settings_page.edit_coustomization_tab()
        restaurant_settings_page.get_vaules_coustomization_tab()

        Assert.equal(restaurant_settings_page._percentage_of_capacity_labeled_as_confirmed_value, restaurant_settings_page._percentage_of_capacity_labeled_as_confirmed_saved_value, "The value of percentage of capacity labeled as confirmed in coustomizations tab isn't equal to the edited value")
        Assert.equal(restaurant_settings_page._booking_in_advance_value, restaurant_settings_page._booking_in_advance_saved_value, "The value of booking in advance in coustomizations tab isn't equal to the edited value")

    def test_add_daily_note_for_staff_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(home_page.header._einloggen_text, "Einloggen"),"\"Einloggen\" text wasn't found on the login page")
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_registered_restaurant("AUTOTESTa")
        account_page.open_shifts_menu()
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(account_page._click_first_shift_button), "The first shift wasn't found on the shifts menu page")
        while True:
            if account_page._added_note_type_guests_value in account_page.get_page_source().encode('utf-8'):
                account_page.remove_added_note()
            if account_page._added_note_type_staff_value in account_page.get_page_source().encode('utf-8'):
                account_page.remove_added_note()
            if not account_page._added_note_type_guests_value in account_page.get_page_source().encode('utf-8') and not account_page._added_note_type_staff_value in account_page.get_page_source().encode('utf-8'):
                break
        account_page.add_note_for_staff()
        account_page.click_add_notes_button()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(account_page._added_note_value_field, account_page._add_note_text_value), "The addded note text isn't visible in the appropriate field on the shifts menu page, probably the note wasn't added or is visible in the wrong place")
        account_page.get_text_added_note_type()
        Assert.equal(account_page.added_note_type_text, account_page._added_note_type_staff_value, "The added note type (For Staff) is not visible in the right place")

        account_page.remove_added_note()

        self.not_contains(account_page._added_note_type_staff_value, account_page.get_page_source().encode('utf-8'), "The added note type (For Staff) is present on the page source although it shouldn't be because the note should was supposed to be removed")
        self.not_contains(account_page._add_note_text_value, account_page.get_page_source(), "The added note text is present on the page source although it shouldn't be because the note should was supposed to be removed")

    def test_add_daily_note_for_guests_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(home_page.header._einloggen_text, "Einloggen"),"\"Einloggen\" text wasn't found on the login page")
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_registered_restaurant("AUTOTESTa")
        account_page.open_shifts_menu()
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(account_page._click_first_shift_button), "The first shift wasn't found on the shifts menu page")
        while True:
            if account_page._added_note_type_guests_value in account_page.get_page_source().encode('utf-8'):
                account_page.remove_added_note()
            if account_page._added_note_type_staff_value in account_page.get_page_source().encode('utf-8'):
                account_page.remove_added_note()
            if not account_page._added_note_type_guests_value in account_page.get_page_source().encode('utf-8') and not account_page._added_note_type_staff_value in account_page.get_page_source().encode('utf-8'):
                break
        account_page.add_note_for_guests()
        account_page.click_add_notes_button()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(account_page._added_note_value_field, account_page._add_note_text_value), "The addded note text isn't visible in the appropriate field on the shifts menu page, probably the note wasn't added or is visible in the wrong place")
        account_page.get_text_added_note_type()
        Assert.equal(account_page.added_note_type_text, account_page._added_note_type_guests_value, "The added note type (For Guests) is not visible in the right place")

        account_page.remove_added_note()

        self.not_contains(account_page._added_note_type_guests_value, account_page.get_page_source().encode('utf-8'), "The added note type (For Guests) is present on the page source although it shouldn't be because the note should was supposed to be removed")
        self.not_contains(account_page._add_note_text_value, account_page.get_page_source(), "The added note text is present on the page source although it shouldn't be because the note should was supposed to be removed")

    def test_add_reservation_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(home_page.header._einloggen_text, "Einloggen"),"\"Einloggen\" text wasn't found on the login page")
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_registered_restaurant("George Bar & Grill")
        account_page.open_shifts_menu()
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(account_page._click_first_shift_button), "The first shift wasn't found on the shifts menu page")
        sleep(2)
        account_page.get_first_shift_start_time()
        seatIn_page = account_page.click_first_shift()
        # seatIn_page = account_page.open_seatIn()
        # seatIn_page.click_hour()
        seatIn_page.click_add_reservation_plus_button()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(seatIn_page._seatIn_room_separator_field), "The room separator field wasn't found on the SeatIn page")
        seatIn_page.click_reservation_details_button()
        seatIn_page.enter_reservation_details(account_page.first_shift_start_time)
        seatIn_page.save_reservation()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(seatIn_page._seatIn_room_separator_field), "The room separator field wasn't found on the SeatIn page")
        seatIn_page.expand_seatIn_reservation_details()

        Assert.contains(seatIn_page._add_reservation_surname_value, seatIn_page.get_page_source(), "The added reservation surname value wasn't found in the added reservations in SeatIn page, probably the reservation wasn't added")
        # Assert.contains(seatIn_page._add_reservation_guests_comment_value, seatIn_page.get_page_source())
        # Assert.contains(seatIn_page._add_reservation_internal_comment_value, seatIn_page.get_page_source())

        seatIn_page.click_added_reservation()
        seatIn_page.click_added_reservation()
        seatIn_page.remove_added_reservation()

        self.not_contains(seatIn_page._add_reservation_surname_value, seatIn_page.get_page_source(), "The added reservation surname value was found in the added reservations page in SeatIn, although it shouldn't be, because the reservation was supposed to be removed")

    def test_add_provisional_reservation_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(home_page.header._einloggen_text, "Einloggen"),"\"Einloggen\" text wasn't found on the login page")
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_registered_restaurant("George Bar & Grill")
        account_page.open_shifts_menu()
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(account_page._click_first_shift_button), "The first shift wasn't found on the shifts menu page")
        sleep(2)
        account_page.get_first_shift_start_time()
        seatIn_page = account_page.click_first_shift()
        # seatIn_page = account_page.open_seatIn()
        # seatIn_page.click_hour()
        seatIn_page.click_add_reservation_plus_button()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(seatIn_page._seatIn_room_separator_field), "The room separator field wasn't found on the SeatIn page")
        seatIn_page.click_reservation_details_button()
        seatIn_page.enter_reservation_details(account_page.first_shift_start_time)
        seatIn_page.reservation_set_provisional()
        seatIn_page.save_reservation()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(seatIn_page._seatIn_room_separator_field), "The room separator field wasn't found on the SeatIn page")
        seatIn_page.expand_seatIn_reservation_details()

        Assert.contains(seatIn_page._add_reservation_surname_value, seatIn_page.get_page_source(), "The added reservation surname value wasn't found in the added reservations in SeatIn page, probably the reservation wasn't added")
        # Assert.contains(seatIn_page._add_reservation_guests_comment_value, seatIn_page.get_page_source())
        # Assert.contains(seatIn_page._add_reservation_internal_comment_value, seatIn_page.get_page_source())
        Assert.contains("Provisorisch", seatIn_page.get_page_source(), "The text \"Provisorisch\" wasn't found in the added reservations in SeatIn page, the reservation wasn't set provisional")

        seatIn_page.click_added_reservation()
        seatIn_page.click_added_reservation()
        seatIn_page.remove_added_reservation()

        self.not_contains(seatIn_page._add_reservation_surname_value, seatIn_page.get_page_source(), "The added reservation surname value was found in the added reservations page in SeatIn, although it shouldn't be, because the reservation was supposed to be removed")

    def test_edit_reservation_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(home_page.header._einloggen_text, "Einloggen"),"\"Einloggen\" text wasn't found on the login page")
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_registered_restaurant("George Bar & Grill")
        account_page.open_shifts_menu()
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(account_page._click_first_shift_button), "The first shift wasn't found on the shifts menu page")
        sleep(2)
        account_page.get_first_shift_start_time()
        seatIn_page = account_page.click_first_shift()
        # seatIn_page = account_page.open_seatIn()
        # seatIn_page.click_hour()
        seatIn_page.click_add_reservation_plus_button()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(seatIn_page._seatIn_room_separator_field), "The room separator field wasn't found on the SeatIn page")
        seatIn_page.click_reservation_details_button()
        seatIn_page.enter_reservation_details(account_page.first_shift_start_time)
        seatIn_page.save_reservation()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(seatIn_page._seatIn_room_separator_field), "The room separator field wasn't found on the SeatIn page")
        seatIn_page.expand_seatIn_reservation_details()

        Assert.contains(seatIn_page._add_reservation_surname_value, seatIn_page.get_page_source(), "The added reservation surname value wasn't found in the added reservations in SeatIn page, probably the reservation wasn't added")
        # Assert.contains(seatIn_page._add_reservation_guests_comment_value, seatIn_page.get_page_source())
        # Assert.contains(seatIn_page._add_reservation_internal_comment_value, seatIn_page.get_page_source())

        seatIn_page.click_added_reservation()
        seatIn_page.click_added_reservation()
        seatIn_page.remove_added_reservation()

        self.not_contains(seatIn_page._add_reservation_surname_value, seatIn_page.get_page_source(), "The added reservation surname value was found in the added reservations page in SeatIn, although it shouldn't be, because the reservation was supposed to be removed")
        #do napisania

    def test_add_daily_shift_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(home_page.header._einloggen_text, "Einloggen"),"\"Einloggen\" text wasn't found on the login page")
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_registered_restaurant("AUTOTESTb")
        daily_settings_page = account_page.open_daily_settings()
        sleep(3)
        while True:
            if daily_settings_page._add_daily_shift_name_value in daily_settings_page.get_page_source():
                daily_settings_page.remove_first_daily_shift()
            if not daily_settings_page._add_daily_shift_name_value in daily_settings_page.get_page_source():
                break
        daily_settings_page.add_daily_shift_click_button()
        daily_settings_page.add_shift_daily_first_accordeon()
        daily_settings_page.add_shift_second_accordeon()
        daily_settings_page.save_shift()
        seatIn_page = account_page.open_seatIn()

        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(seatIn_page._shift_name_field, daily_settings_page._add_daily_shift_name_value), "The added daily shift name wasn't found in the shift name field in SeatIn, so probably the default shift didn't change to daily shift")

        HomePage(self.driver).open_home_page()
        daily_settings_page = account_page.open_daily_settings()
        daily_settings_page.remove_first_daily_shift()

        self.not_contains(daily_settings_page._add_daily_shift_name_value, daily_settings_page.get_page_source(), "The daily shift name vaule was found in the daily shifts page source, although it shouldn't be, because the daily shift is supposed to be removed")

# chyba trzeba poprawić sprawdzanie po dodaniu shifta

    def test_edit_daily_shift_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(home_page.header._einloggen_text, "Einloggen"),"\"Einloggen\" text wasn't found on the login page")
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_registered_restaurant("George Bar & Grill")
        daily_settings_page = account_page.open_daily_settings()
        sleep(3)
        if not "edit-shift" in daily_settings_page.get_page_source():
            daily_settings_page.daily_shift_activate_first_global()
        if not "edit-shift" in daily_settings_page.get_page_source():
            daily_settings_page.daily_shift_activate_first_global()
        daily_settings_page.edit_first_daily_shift()
        daily_settings_page.add_shift_daily_first_accordeon()
        daily_settings_page.save_shift()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(daily_settings_page._first_shift_internal_name_field, daily_settings_page._add_daily_shift_internal_name_value), "The edited daily shift internal name value wasn't found in the first shift internal name field on the daily shift page, probably the shift wasn't edited")
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(daily_settings_page._daily_shift_edit_first_button, daily_settings_page._add_daily_shift_name_value), "The edited daily shift name value wasn't found in the first shift name field on the daily shift page, probably the shift wasn't edited")

        daily_settings_page.daily_shift_activate_first_global()

        self.not_contains(daily_settings_page._add_daily_shift_name_value, daily_settings_page.get_page_source(), "The daily shift name value was found in the daily shifts page source, although it shouldn't be, because the daily shift is supposed to be substituted by global shift")
        self.not_contains(daily_settings_page._add_daily_shift_internal_name_value, daily_settings_page.get_page_source(), "The daily shift internal name value was found in the daily shifts page source, although it shouldn't be, because the daily shift is supposed to be substituted by global shift")

#nie działa zmiana na global shift, zgłoszone

    def test_add_contact_to_relatin_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(home_page.header._einloggen_text, "Einloggen"),"\"Einloggen\" text wasn't found on the login page")
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_registered_restaurant("AUTOTESTa")
        relatIn_page = account_page.open_relatIn()
        relatIn_page.add_client()

        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(relatIn_page._added_client_first_name_field, relatIn_page._client_first_name_value), "The added client first name value didn't appear in the first name field of the first client on the relatIn page, probably the client wasn't added or the text was shown in the wrong place")
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(relatIn_page._added_client_last_name_field, relatIn_page._client_last_name_value), "The added client last name value didn't appear in the last name field of the first client on the relatIn page, probably the client wasn't added or the text was shown in the wrong place")
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(relatIn_page._added_client_phone_number_field, "+41"+relatIn_page._client_phone_number_value), "The added client phone number value didn't appear in the phone number field of the first client on the relatIn page, probably the client wasn't added or the text was shown in the wrong place")
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(relatIn_page._added_client_email_field, relatIn_page._client_email_value), "The added client email value didn't appear in the email field of the first client on the relatIn page, probably the client wasn't added or the text was shown in the wrong place")
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(relatIn_page._added_client_category_field, relatIn_page._client_category_value), "The added client category value didn't appear in the category field of the first client on the relatIn page, probably the client wasn't added or the text was shown in the wrong place")

        relatIn_page.remove_first_client()

        WebDriverWait(self.driver, 10).until_not(EC.text_to_be_present_in_element(relatIn_page._added_client_first_name_field, relatIn_page._client_first_name_value), "The added client first name value appeared in the first name field of the first client on the relatIn page, although it shouldn't, because the client was supposed to be removed")
        self.not_contains(relatIn_page._client_last_name_value, relatIn_page.get_page_source(), "The added client last name value appeared on the relatIn page, although it shouldn't, because the client was supposed to be removed")
        self.not_contains(relatIn_page._client_phone_number_value, relatIn_page.get_page_source(), "The added client phone number value appeared on the relatIn page, although it shouldn't, because the client was supposed to be removed")
        self.not_contains(relatIn_page._client_email_value, relatIn_page.get_page_source(), "The added client email value appeared on the relatIn page, although it shouldn't, because the client was supposed to be removed")

    def test_zz_generate_plot_and_send_email(self):
        self._save_plot()
        self._send_email()

    def tally(self):
        return len(self._resultForDoCleanups.errors) + len(self._resultForDoCleanups.failures)

    def setUp(self):
        self.timeout = 30
        if run_locally:
            fp = webdriver.FirefoxProfile()
            fp.set_preference("browser.startup.homepage", "about:blank")
            fp.set_preference("startup.homepage_welcome_url", "about:blank")
            fp.set_preference("startup.homepage_welcome_url.additional", "about:blank")
            fp.set_preference(" xpinstall.signatures.required", "false")
            fp.set_preference("toolkit.telemetry.reportingpolicy.firstRun", "false")
            binary = FirefoxBinary('/__stare/firefox45/firefox')
            self.driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp)
            self.driver.set_window_size(1024,768)
            self.driver.implicitly_wait(self.timeout)
            self.errors_and_failures = self.tally()
        else:
            self.desired_capabilities['name'] = self.id()
            sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"

            self.driver = webdriver.Remote(
                desired_capabilities=self.desired_capabilities,
                command_executor=sauce_url % (USERNAME, ACCESS_KEY)
            )

            self.driver.implicitly_wait(self.timeout)

    def tearDown(self):
        if run_locally:
                if self.tally() > self.errors_and_failures:
                    if not os.path.exists(SCREEN_DUMP_LOCATION):
                        os.makedirs(SCREEN_DUMP_LOCATION)
                    for ix, handle in enumerate(self.driver.window_handles):
                        self._windowid = ix
                        self.driver.switch_to.window(handle)
                        self.take_screenshot()
                        self.dump_html()
                self.driver.quit()

    def _get_filename(self):
        timestamp = datetime.now().isoformat().replace(':', '.')[:19]
        self._saved_filename = "{classname}.{method}-window{windowid}-{timestamp}".format(
            classname=self.__class__.__name__,
            method=self._testMethodName,
            windowid=self._windowid,
            timestamp=timestamp
        )
        return "{folder}/{classname}.{method}-window{windowid}-{timestamp}".format(
            folder=SCREEN_DUMP_LOCATION,
            classname=self.__class__.__name__,
            method=self._testMethodName,
            windowid=self._windowid,
            timestamp=timestamp
        )

    def _get_filename_for_plot(self):
        timestamp = datetime.now().isoformat().replace(':', '.')[:19]
        self._saved_filename_plot = "{classname}.plot-{timestamp}".format(
            classname=self.__class__.__name__,
            timestamp=timestamp
        )
        return "{folder}/{classname}.plot-{timestamp}".format(
            folder=SCREEN_DUMP_LOCATION,
            classname=self.__class__.__name__,
            timestamp=timestamp
            )

    def _save_plot(self):
        import matplotlib.pyplot as plt
        filename = self._get_filename_for_plot() + ".png"
        err = len(self._resultForDoCleanups.errors)
        fail = len(self._resultForDoCleanups.failures)

        # The slices will be ordered and plotted counter-clockwise.
        labels = 'Errors', 'Failures', 'Passes'
        sizes = [err, fail, 18-fail-err]
        colors = ['red', 'gold', 'green']
        explode = (0.1, 0.1, 0.1)

        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        print "\n WYKRES:\n", filename
        plt.savefig(filename)
        text_file = open("AlenoRaportScreeny.txt", "a")
        text_file.write("<br><br>Wykres statystyczny: <a href=""http://ci.testuj.pl/job/Aleno/ws/screendumps/"+self._saved_filename_plot+".png>Wykres</a>")
        text_file.close()

    def take_screenshot(self):
        filename = self._get_filename() + ".png"
        print "\n{method} Screenshot and HTML:\n".format(
            method=self._testMethodName)
        print 'screenshot:', filename
        self.driver.get_screenshot_as_file(filename)
        text_file = open("AlenoRaportScreeny.txt", "a")
        text_file.write("<br><br>{method} Screenshot and HTML:<br>".format(
            method=self._testMethodName)+"<br>Screenshot: <a href=""http://ci.testuj.pl/job/Aleno/ws/screendumps/"+self._saved_filename+".png>"+self._saved_filename+"</a>")
        text_file.close()

    def dump_html(self):
        filename = self._get_filename() + '.html'
        print 'page HTML:', filename
        with open(filename, 'w') as f:
            f.write(self.driver.page_source.encode('utf-8'))
        text_file = open("AlenoRaportScreeny.txt", "a")
        text_file.write("<br>Html: <a href=""http://ci.testuj.pl/job/Aleno/ws/screendumps/"+self._saved_filename+".html>"+self._saved_filename+"</a>")
        text_file.close()

    def _send_email(self):
        from mailer import Mailer
        from mailer import Message

        message = Message(From="jedrzej.wojcieszczyk@testuj.pl",
                          To=["jedrzej.wojcieszczyk@testuj.pl"])
        message.Subject = "Raport Jenkins Aleno Testy Automatyczne"
        message.Html = """<head><meta http-equiv="Content-Type" content="text/html;charset=UTF-8"></head><p>Cześć!<br>
           Oto wygenerowany automatycznie raport z testów Aleno.pl<br><br>
           Tabela raportowa z logami wykonanych testów, a pod nią linki do screenshotów i kodu html testów które nie przeszły oraz wykres statystyczny: <a href="http://ci.testuj.pl/job/Aleno/ws/AlenoReportLogi.html">Tabela z logami, screenshoty i wykres</a></p>"""

        sender = Mailer('smtp.gmail.com', use_tls=True, usr='jedrzej.wojcieszczyk@testuj.pl', pwd='paluch88')
        sender.send(message)

    def not_contains(self, needle, haystack, msg=''):
        try:
            assert not needle in haystack
        except AssertionError:
            raise AssertionError('%s is found in %s. %s' % (needle, haystack, msg))

    def is_element_present(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

open("AlenoRaportScreeny.txt", 'w').close()
suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTest)
outfile = open("AlenoReportLogi.html", "wb")
runner = HTMLTestRunner(stream=outfile, title='Test Report', description='Aleno', verbosity=2)
runner.run(suite)

     # htmltestrunner.main()
# if __name__ == '__main__':
#      unittest.main()

     # import xmlrunner
     # unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))