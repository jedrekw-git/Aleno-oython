# coding=utf-8
import unittest
from selenium import webdriver
from unittestzero import Assert
from pages.home import HomePage
from utils.config import *
from utils.utils import *
from datetime import timedelta, date
from time import sleep
import os
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import gmtime, strftime
import re

SCREEN_DUMP_LOCATION = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'screendumps'
)
run_locally = True

# @on_platforms(browsers)
class SmokeTest(unittest.TestCase):

    def test_login_and_logout_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        home_page.header.logout()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(account_page._einloggen_text_field, "Einloggen"))

    def test_register_restaurant_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            home_page.header.login(USER, PASSWORD)
        register_restaurant_page = home_page.header.open_register_restaurant_page()
        register_restaurant_page.enter_restaurant_data()
        account_page = register_restaurant_page.save_restaurant()
        sleep(6)
        restaurant_settings_page = account_page.open_restaurant_settings()
        restaurant_settings_page.get_restaurant_info()

        Assert.equal(restaurant_settings_page.restaurant_info_last_name, register_restaurant_page._last_name_value)
        Assert.equal(restaurant_settings_page.restaurant_info_address, register_restaurant_page._address_value)
        Assert.equal(restaurant_settings_page.restaurant_info_zip, register_restaurant_page._zip_code_value)
        Assert.equal(restaurant_settings_page.restaurant_info_city, register_restaurant_page._city_value)
        Assert.equal(restaurant_settings_page.restaurant_info_country, register_restaurant_page._country_value)
        Assert.equal(restaurant_settings_page.restaurant_info_email, register_restaurant_page._email_value)
        Assert.equal(restaurant_settings_page.restaurant_info_senders_email, register_restaurant_page._senders_email_value)
        Assert.equal(restaurant_settings_page.restaurant_info_msgIn_email, register_restaurant_page._msgIn_email_value)
        Assert.equal(restaurant_settings_page.restaurant_info_website, register_restaurant_page._website_value)
        Assert.equal(restaurant_settings_page.restaurant_info_facebook, register_restaurant_page._facebook_value)
        Assert.equal(restaurant_settings_page.restaurant_info_fan_page, register_restaurant_page._fan_page_url_value)
        Assert.equal(restaurant_settings_page.restaurant_info_trip_advisor, register_restaurant_page._trip_advisor_value)
        Assert.equal(restaurant_settings_page.restaurant_info_google, register_restaurant_page._google_value)
        Assert.equal(restaurant_settings_page.restaurant_info_yelp, register_restaurant_page._yelp_value)
        Assert.equal(restaurant_settings_page.restaurant_info_phone, register_restaurant_page._phone_value)
        Assert.equal(restaurant_settings_page.restaurant_info_image_url, register_restaurant_page._image_url_value)

    def test_add_rooms_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_AUTOTESTafnssmwc_restaurant()
        restaurant_settings_page = account_page.open_restaurant_settings()
        restaurant_settings_page.open_rooms_tab()
        restaurant_settings_page.add_two_rooms()
        restaurant_settings_page.remove_added_rooms()

        self.not_contains(restaurant_settings_page._add_room_name_value1, restaurant_settings_page.get_page_source())
        self.not_contains(restaurant_settings_page._add_room_name_value2, restaurant_settings_page.get_page_source())

#Dodawanie pokoju po angielsku jest niemożliwe, zgłoszone

    def test_add_shift_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_AUTOTESTafnssmwc_restaurant()
        restaurant_settings_page = account_page.open_restaurant_settings()
        restaurant_settings_page.open_shift_tab()
        restaurant_settings_page.add_shift_first_accordeon()
        restaurant_settings_page.add_shift_second_accordeon()
        restaurant_settings_page.save_shift()
        restaurant_settings_page.open_first_shift_details()
        restaurant_settings_page.first_shift_get_values()

        Assert.equal(restaurant_settings_page.added_shift_name, restaurant_settings_page._shift_name_value)
        Assert.equal(restaurant_settings_page.added_shift_internal_name, restaurant_settings_page._shift_internal_name_value)
        # Assert.equal(restaurant_settings_page.added_shift_capacity, restaurant_settings_page._shift_capacity_value)
        Assert.equal(restaurant_settings_page.added_shift_buffer, restaurant_settings_page._shift_buffer_value)
        Assert.equal(restaurant_settings_page.added_shift_daily_deadlinie, restaurant_settings_page._shift_daily_online_deadline_value)
        Assert.equal(restaurant_settings_page.added_shift_kitchen_start, restaurant_settings_page._shift_kitchen_start_value)
        Assert.equal(restaurant_settings_page.added_shift_kitchen_end, restaurant_settings_page._shift_kitchen_end_value)
        Assert.equal(restaurant_settings_page.added_shift_timeslot_capacity, restaurant_settings_page._shift_timeslot_capacity_value)
        Assert.equal(restaurant_settings_page.added_shift_reservations_confirmed, restaurant_settings_page._shift_reservations_confirmed_value)
        Assert.equal(restaurant_settings_page.added_shift_minimum_guests, restaurant_settings_page._shift_minimum_guests_value)
        Assert.equal(restaurant_settings_page.added_shift_maximum_guests, restaurant_settings_page._shift_maximum_guests_value)

        restaurant_settings_page = account_page.open_restaurant_settings()
        restaurant_settings_page.open_shift_tab()
        restaurant_settings_page.remove_first_shift()

        self.not_contains(restaurant_settings_page._shift_name_value, restaurant_settings_page.get_page_source())
        self.not_contains(restaurant_settings_page._shift_internal_name_value, restaurant_settings_page.get_page_source())

#Dodawanie shifta po angielsku jest niemożliwe, zgłoszone

    def test_add_room_to_shift_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_AUTOTESTagfkzhye_restaurant()
        restaurant_settings_page = account_page.open_restaurant_settings()
        restaurant_settings_page.open_shift_tab()
        restaurant_settings_page.add_shift_first_accordeon()
        restaurant_settings_page.add_1_room_to_shift()
        restaurant_settings_page.save_shift()

        account_page = home_page.header.open_account_page()
        account_page.open_shifts_menu()
        account_page.expand_first_shift()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(account_page._first_shift_first_room_name_field, restaurant_settings_page.first_room_name))

        account_page = home_page.header.open_account_page()
        restaurant_settings_page = account_page.open_restaurant_settings()
        restaurant_settings_page.open_shift_tab()
        restaurant_settings_page.remove_first_shift()

        self.not_contains(restaurant_settings_page._shift_name_value, restaurant_settings_page.get_page_source())
        self.not_contains(restaurant_settings_page._shift_internal_name_value, restaurant_settings_page.get_page_source())

#Dodawanie shifta po angielsku jest niemożliwe, zgłoszone

    def test_add_2_rooms_to_shift_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_AUTOTESTagfkzhye_restaurant()
        restaurant_settings_page = account_page.open_restaurant_settings()
        restaurant_settings_page.open_shift_tab()
        restaurant_settings_page.add_shift_first_accordeon()
        restaurant_settings_page.add_shift_second_accordeon()
        restaurant_settings_page.add_2_rooms_to_shift_publish()
        restaurant_settings_page.save_shift()

        account_page = home_page.header.open_account_page()
        account_page.open_shifts_menu()
        account_page.expand_first_shift()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(account_page._first_shift_first_room_name_field, restaurant_settings_page.first_room_name))
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(account_page._first_shift_second_room_name_field, restaurant_settings_page.second_room_name))

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

        account_page = home_page.header.open_account_page()
        restaurant_settings_page = account_page.open_restaurant_settings()
        restaurant_settings_page.open_shift_tab()
        restaurant_settings_page.remove_first_shift()

        self.not_contains(restaurant_settings_page._shift_name_value, restaurant_settings_page.get_page_source())
        self.not_contains(restaurant_settings_page._shift_internal_name_value, restaurant_settings_page.get_page_source())

#NIE WIDZI POPUP'U

    def test_add_reservation_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_AUTOTESTazejgfmg_restaurant()
        seatIn_page = account_page.open_seatIn()
        seatIn_page.click_hour()
        seatIn_page.click_add_reservation_plus_button()
        seatIn_page.click_reservation_details_button()
        seatIn_page.enter_reservation_details()
        seatIn_page.save_reservation()
        seatIn_page.expand_seatIn_reservation_details()

        Assert.contains(seatIn_page._add_reservation_surname_value, seatIn_page.get_page_source())
        Assert.contains(seatIn_page._add_reservation_guests_comment_value, seatIn_page.get_page_source())
        Assert.contains(seatIn_page._add_reservation_internal_comment_value, seatIn_page.get_page_source())

        seatIn_page.click_added_reservation()
        seatIn_page.remove_added_reservation()

#AUTOMATYCZNY TEST NIE DODAJE REZERWACJI

    def test_add_provisional_reservation_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_AUTOTESTazejgfmg_restaurant()
        account_page = home_page.header.open_account_page()
        account_page.open_shifts_menu()
        account_page.click_first_shift()
        seatIn_page = account_page.open_seatIn()
        seatIn_page.click_hour()
        seatIn_page.click_add_reservation_plus_button()
        seatIn_page.click_reservation_details_button()
        seatIn_page.enter_reservation_details()
        seatIn_page.reservation_set_provisional()
        seatIn_page.save_reservation()
        account_page = home_page.header.open_account_page()
        account_page.open_shifts_menu()
        account_page.click_first_shift()
        seatIn_page = account_page.open_seatIn()
        seatIn_page.expand_seatIn_reservation_details()

        Assert.contains(seatIn_page._add_reservation_surname_value, seatIn_page.get_page_source())
        # Assert.contains(seatIn_page._add_reservation_guests_comment_value, seatIn_page.get_page_source())
        # Assert.contains(seatIn_page._add_reservation_internal_comment_value, seatIn_page.get_page_source())
        Assert.contains("Provisional", seatIn_page.get_page_source())

        seatIn_page.click_added_reservation()
        seatIn_page.remove_added_reservation()

#AUTOMATIC RESERVATION ISN'T CREATED, zgłoszone

    def test_edit_reservation_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_AUTOTESTazejgfmg_restaurant()
        account_page = home_page.header.open_account_page()
        account_page.open_shifts_menu()
        account_page.click_first_shift()
        seatIn_page = account_page.open_seatIn()
        seatIn_page.click_hour()
        seatIn_page.click_reservation_details_button()
        seatIn_page.reservation_open_first_accordeon()
        seatIn_page.enter_reservation_details()
        seatIn_page.reservation_set_email_sms_notifications()
        seatIn_page.save_reservation()

#DO POPRAWKI PO NAPRAWIE DODAWANIA REZERWACJI

    def test_add_daily_shift_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_AUTOTESTazejgfmg_restaurant()
        daily_settings_page = account_page.open_daily_settings()
        sleep(3)
        daily_settings_page.add_daily_shift_click_button()
        daily_settings_page.add_shift_daily_first_accordeon()
        daily_settings_page.add_shift_second_accordeon()
        daily_settings_page.save_shift()
        seatIn_page = account_page.open_seatIn()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(seatIn_page._shift_name_field, daily_settings_page._add_daily_shift_name_value))

        HomePage(self.driver).open_home_page()
        daily_settings_page = account_page.open_daily_settings()
        daily_settings_page.remove_first_daily_shift()

        self.not_contains(daily_settings_page._add_daily_shift_name_value, daily_settings_page.get_page_source())

# trzeba najpierw kliknąć "EN-gb" zanim pojawi sie pole tekstowe, ma tak być?

    def test_edit_daily_shift_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        sleep(5)
        if "Einloggen" in home_page.header.get_page_source():
            account_page = home_page.header.login(USER, PASSWORD)
        account_page.open_AUTOTESTazejgfmg_restaurant()
        daily_settings_page = account_page.open_daily_settings()
        sleep(3)
        daily_settings_page.daily_shift_activate_global()
        daily_settings_page.edit_first_daily_shift()
        daily_settings_page.add_shift_daily_first_accordeon()
        daily_settings_page.save_shift()
        sleep(2)

        Assert.contains(daily_settings_page._add_daily_shift_name_value, daily_settings_page.get_page_source())
        Assert.contains(daily_settings_page._add_daily_shift_internal_name_value, daily_settings_page.get_page_source())

        daily_settings_page.daily_shift_activate_global()

        self.not_contains(daily_settings_page._add_daily_shift_name_value, daily_settings_page.get_page_source())
        self.not_contains(daily_settings_page._add_daily_shift_internal_name_value, daily_settings_page.get_page_source())

    def tally(self):
        return len(self._resultForDoCleanups.errors) + len(self._resultForDoCleanups.failures)

    def setUp(self):
        self.timeout = 30
        if run_locally:
            # fp = webdriver.FirefoxProfile()
            # fp.set_preference("browser.startup.homepage", "about:blank")
            # fp.set_preference("startup.homepage_welcome_url", "about:blank")
            # fp.set_preference("startup.homepage_welcome_url.additional", "about:blank")
            # fp.set_preference("xpinstall.signatures.required", "false")
            # fp.set_preference("toolkit.telemetry.reportingpolicy.firstRun", "false")
            # fp.set_preference('general.warnOnAboutConfig', "False")
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
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
                        # self.take_screenshot()
                        # self.dump_html()
                self.driver.quit()

    def not_contains(self, needle, haystack, msg=''):
        try:
            assert not needle in haystack
        except AssertionError:
            raise AssertionError('%s is found in %s. %s' % (needle, haystack, msg))

if __name__ == '__main__':
     unittest.main()
