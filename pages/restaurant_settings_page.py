# coding=utf-8
from selenium.webdriver.common.by import By
from pages.base import BasePage
from utils.utils import *
from random import randint
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import datetime

class RestaurantSettingsPage(BasePage):
    _title = "Restaurant Settings Page"

    _last_name_field = (By.NAME, "name")
    _address_field = (By.NAME, "address")
    _zip_code_field = (By.NAME, "zipcode")
    _city_field = (By.NAME, "city")
    _country_field = (By.NAME, "country")
    _email_field = (By.NAME, "email")
    _senders_email_field = (By.NAME, "publicEmail")
    _msgIn_email_field = (By.NAME, "msgInEmail")
    _website_field = (By.NAME, "website")
    _facebook_field = (By.NAME, "facebook")
    _fan_page_url_field = (By.NAME, "fanPageUrl")
    _trip_advisor_field = (By.NAME, "tripadvisor")
    _google_field = (By.NAME, "google")
    _yelp_field = (By.NAME, "yelp")
    _phone_field = (By.NAME, "phone")
    _image_url_field = (By.NAME, "imageUrl")
    _rooms_tab = (By.XPATH, "//div/ul/li[4]/a")
    _add_room_en_button = (By.XPATH, "//form/div/div[4]/button[2]")
    _add_room_name_field = (By.XPATH, "//form/div/div[2]/input")
    _add_room_name_value1 = get_random_string(8)
    _add_room_name_value2 = get_random_string(7)
    _add_room_submit = (By.XPATH, "//div[2]/form/button")
    _add_room_capacity_field1 = (By.NAME, "capacity")
    _add_room_capacity_field2 = (By.XPATH, "//div[2]/div/div/div[2]/form/div[2]/input")
    _add_room_capacity_value = "20"
    _add_room_bookable_field1 = (By.NAME, "bookable")
    _add_room_bookable_field2 = (By.XPATH, "//div[2]/div/div/div[2]/form/div[3]/input")
    _add_room_bookable_value = "10"
    _add_room_order_field1 = (By.NAME, "order")
    _add_room_order_field2 = (By.XPATH, "//div[2]/div/div/div[2]/form/div[4]/input")
    _add_room_order_value1 = "1"
    _add_room_order_value2 = "2"
    _add_room_remove_first = (By.XPATH, "//div/div/div/a")
    _shift_tab = (By.XPATH, "//div/ul/li[2]/a")
    _add_shift_button = (By.XPATH, "/html/body/div[2]/div[2]/div/div/button")
    _shift_name_field = (By.XPATH, "//div[2]/input")
    _shift_name_value = "Shift Abend"
    _shift_internal_name_field = (By.XPATH, "//div[2]/div/div[2]/input")
    _shift_internal_name_value = "abend"
    _shift_start_date_field = (By.NAME, "startDate")
    _shift_start_date_value = str(datetime.date.today().day-1)+"."+str(datetime.date.today().month)+"."+str(datetime.date.today().year)
    _shift_service_start_field = (By.NAME, "openingTime")
    _shift_service_start_value = "16:00"
    _shift_service_end_field = (By.NAME, "closingTime")
    _shift_service_end_value = "22:00"
    _shift_second_accordeon_menu = (By.LINK_TEXT, "Reservation")
    _shift_reservation_requirements_checkbox = (By.NAME, "isEnabled")
    _shift_capacity_field = (By.NAME, "availableSeats")
    _shift_capacity_value = "100"
    _shift_reservations_confirmed_field = (By.NAME, "capacityTechnically")
    _shift_reservations_confirmed_value = "80"
    _shift_buffer_field = (By.NAME, "buffer")
    _shift_buffer_value = "20"
    _shift_daily_online_deadline_field = (By.NAME, 'dailyDeadline')
    _shift_daily_online_deadline_value = "10:00"
    _shift_kitchen_start_field = (By.NAME, "startTime")
    _shift_kitchen_start_value = "16:00"
    _shift_kitchen_end_field = (By.NAME, "endTime")
    _shift_kitchen_end_value = "22:00"
    _shift_duration_of_reservation_field = (By.NAME, "stayTime")
    _shift_duration_of_reservation_value = "120"
    _shift_timeslot_capacity_field = (By.NAME, "maxPerTimeslot")
    _shift_timeslot_capacity_value = "20"
    _shift_minimum_guests_field = (By.NAME, "peopleCountMin")
    _shift_minimum_guests_value = "2"
    _shift_maximum_guests_field = (By.NAME, "peopleCountMax")
    _shift_maximum_guests_value = "8"
    _shift_save_button = (By.XPATH, "//div[2]/button")
    _added_shift_show_copies_button = (By.XPATH, "//td[6]/button[2]")
    _added_shift_name_field = (By.NAME, "name")
    _added_shift_internal_name_field = (By.NAME, "internalName")
    _remove_added_shift_button = (By.XPATH, "//td[6]/button")
    _shift_third_accordeon_menu = (By.LINK_TEXT, "Rooms")
    _shift_select_first_room_checkbox = (By.NAME, "roomId")
    _shift_first_room_name_field = (By.XPATH, "//div[2]/div/div/div/div/div/div/div")
    _shift_second_room_name_field = (By.XPATH, "//div[2]/div/div/div/div/div/div[2]/div")
    _shift_select_first_room_publish_checkbox = (By.NAME, "publishRoomId")
    _shift_select_second_room_publish_checkbox = (By.XPATH, "//div[2]/div[2]/div/div[4]/div/input")
    _add_daily_shift_button = (By.XPATH, "/html/body/div[2]/div[2]/div/div/button")
    _add_daily_shift_name_value = "Daily Shift Abend"
    _add_daily_shift_internal_name_value = "Daily abend"
    _remove_first_daily_shift_button = (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/table/tbody/tr/td[6]/button")
    _daily_shift_activate_global_checkbox = (By.NAME, "selectedGlobalShifts")
    _daily_shift_activate_global_save_button = (By.XPATH, "/html/body/div[2]/div[2]/div/div/form/button")
    _daily_shift_edit_first_button = (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/table/tbody/tr/td[1]/a")

    def __init__(self, driver):
        super(RestaurantSettingsPage, self).__init__(driver, self._title)

    def get_restaurant_info(self):
        self.restaurant_info_last_name = self.get_value(self._last_name_field)
        self.restaurant_info_address = self.get_value(self._address_field)
        self.restaurant_info_zip = self.get_value(self._zip_code_field)
        self.restaurant_info_city = self.get_value(self._city_field)
        self.restaurant_info_country = self.get_value(self._country_field)
        self.restaurant_info_email = self.get_value(self._email_field)
        self.restaurant_info_senders_email = self.get_value(self._senders_email_field)
        self.restaurant_info_msgIn_email = self.get_value(self._msgIn_email_field)
        self.restaurant_info_website = self.get_value(self._website_field)
        self.restaurant_info_facebook = self.get_value(self._facebook_field)
        self.restaurant_info_fan_page = self.get_value(self._fan_page_url_field)
        self.restaurant_info_trip_advisor = self.get_value(self._trip_advisor_field)
        self.restaurant_info_google = self.get_value(self._google_field)
        self.restaurant_info_yelp = self.get_value(self._yelp_field)
        self.restaurant_info_phone = self.get_value(self._phone_field)
        self.restaurant_info_image_url = self.get_value(self._image_url_field)

    def open_rooms_tab(self):
        self.click(self._rooms_tab)

    def add_two_rooms(self):
        self.click(self._add_room_en_button)
        self.clear_field_and_send_keys(self._add_room_name_value1, self._add_room_name_field)
        self.click(self._add_room_submit)
        sleep(3)
        self.clear_field_and_send_keys(self._add_room_name_value2, self._add_room_name_field)
        self.click(self._add_room_submit)
        self.clear_field_and_send_keys(self._add_room_capacity_value, self._add_room_capacity_field1)
        self.clear_field_and_send_keys(self._add_room_capacity_value, self._add_room_capacity_field2)
        self.clear_field_and_send_keys(self._add_room_bookable_value, self._add_room_bookable_field1)
        self.clear_field_and_send_keys(self._add_room_bookable_value, self._add_room_bookable_field2)
        self.clear_field_and_send_keys(self._add_room_order_value1, self._add_room_order_field1)
        self.clear_field_and_send_keys(self._add_room_order_value2, self._add_room_order_field2)

    def remove_added_rooms(self):
        self.click(self._add_room_remove_first)
        self.accept_alert()
        sleep(3)
        self.click(self._add_room_remove_first)
        self.accept_alert()
        sleep(3)

    def open_shift_tab(self):
        self.click(self._shift_tab)
        sleep(2)

    def add_shift_first_accordeon(self):
        self.click(self._add_shift_button)
        self.clear_field_and_send_keys(self._shift_name_value, self._shift_name_field)
        self.clear_field_and_send_keys(self._shift_internal_name_value, self._shift_internal_name_field)
        self.clear_field_and_send_keys(self._shift_start_date_value, self._shift_start_date_field)
        self.clear_field_and_send_keys(self._shift_service_start_value, self._shift_service_start_field)
        self.clear_field_and_send_keys(self._shift_service_end_value, self._shift_service_end_field)

    def add_shift_second_accordeon(self):
        self.click(self._shift_second_accordeon_menu)
        self.click(self._shift_reservation_requirements_checkbox)
        sleep(2)
        self.clear_field_and_send_keys(self._shift_capacity_value, self._shift_capacity_field)
        self.clear_field_and_send_keys(self._shift_reservations_confirmed_value, self._shift_reservations_confirmed_field)
        self.clear_field_and_send_keys(self._shift_buffer_value, self._shift_buffer_field)
        self.clear_field_and_send_keys(self._shift_daily_online_deadline_value, self._shift_daily_online_deadline_field)
        self.clear_field_and_send_keys(self._shift_kitchen_start_value, self._shift_kitchen_start_field)
        self.clear_field_and_send_keys(self._shift_kitchen_end_value, self._shift_kitchen_end_field)
        self.clear_field_and_send_keys(self._shift_duration_of_reservation_value, self._shift_duration_of_reservation_field)
        self.clear_field_and_send_keys(self._shift_timeslot_capacity_value, self._shift_timeslot_capacity_field)
        self.clear_field_and_send_keys(self._shift_minimum_guests_value, self._shift_minimum_guests_field)
        self.clear_field_and_send_keys(self._shift_maximum_guests_value, self._shift_maximum_guests_field)

    def save_shift(self):
        self.click(self._shift_save_button)

    def open_first_shift_details(self):
        self.click(self._added_shift_show_copies_button)

    def first_shift_get_values(self):
        self.added_shift_name = self.get_value(self._added_shift_name_field)
        self.added_shift_internal_name = self.get_value(self._added_shift_internal_name_field)
        self.added_shift_capacity = self.get_value(self._shift_capacity_field)
        self.added_shift_buffer = self.get_value(self._shift_buffer_field)
        self.added_shift_daily_deadlinie = self.get_value(self._shift_daily_online_deadline_field)
        self.added_shift_kitchen_start = self.get_value(self._shift_kitchen_start_field)
        self.added_shift_kitchen_end = self.get_value(self._shift_kitchen_end_field)
        self.get_driver().execute_script("window.scrollTo(3000, 0);")
        self.added_shift_timeslot_capacity = self.get_value(self._shift_timeslot_capacity_field)
        self.added_shift_reservations_confirmed = self.get_value(self._shift_reservations_confirmed_field)
        self.added_shift_minimum_guests = self.get_value(self._shift_minimum_guests_field)
        self.added_shift_maximum_guests = self.get_value(self._shift_maximum_guests_field)

    def remove_first_shift(self):
        self.click(self._remove_added_shift_button)
        self.accept_alert()

    def add_1_room_to_shift(self):
        self.click(self._shift_third_accordeon_menu)
        self.first_room_name = self.get_text(self._shift_first_room_name_field)
        self.click(self._shift_select_first_room_checkbox)

    def add_2_rooms_to_shift_publish(self):
        self.click(self._shift_third_accordeon_menu)
        self.first_room_name = self.get_text(self._shift_first_room_name_field)
        self.second_room_name = self.get_text(self._shift_second_room_name_field)
        self.click(self._shift_select_first_room_publish_checkbox)
        self.click(self._shift_select_second_room_publish_checkbox)

    def add_daily_shift_click_button(self):
        self.click(self._add_daily_shift_button)

    def add_shift_daily_first_accordeon(self):
        self.clear_field_and_send_keys(self._add_daily_shift_name_value, self._shift_name_field)
        self.clear_field_and_send_keys(self._add_daily_shift_internal_name_value, self._shift_internal_name_field)
        self.clear_field_and_send_keys(self._shift_service_start_value, self._shift_service_start_field)
        self.clear_field_and_send_keys(self._shift_service_end_value, self._shift_service_end_field)

    def remove_first_daily_shift(self):
        self.click(self._remove_first_daily_shift_button)
        self.accept_alert()

    def daily_shift_activate_global(self):
        self.click(self._daily_shift_activate_global_checkbox)
        self.click(self._daily_shift_activate_global_save_button)

    def edit_first_daily_shift(self):
        self.click(self._daily_shift_edit_first_button)