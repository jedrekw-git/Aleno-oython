# coding=utf-8
from selenium.webdriver.common.by import By
from pages.base import BasePage
from utils.utils import *
from random import randint
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
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
    _add_shift_button = (By.XPATH, "//div[@id='__blaze-root']/div[2]/div[2]/div/div/button")
    _shift_name_field = (By.XPATH, "//div[2]/input")
    _shift_name_value = "Shift Abend"
    _shift_internal_name_field = (By.XPATH, "//div[2]/div/div[2]/input")
    _shift_internal_name_value = "abend"
    _shift_start_date_field = (By.NAME, "startDate")
    _shift_start_date_value = str(datetime.date.today().day-2)+"."+str(datetime.date.today().month)+"."+str(datetime.date.today().year)
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
    _shift_save_button = (By.XPATH, "(//button[@type='button'])[2]")
    _added_shift_show_copies_button = (By.XPATH, "//td[6]/button[2]")
    _added_shift_name_field = (By.NAME, "name")
    _added_shift_internal_name_field = (By.NAME, "internalName")
    _remove_added_shift_button = (By.XPATH, "//td[6]/button")
    _shift_third_accordeon_menu = (By.CSS_SELECTOR, "a[href*='#rooms']")
    _shift_select_first_room_checkbox = (By.NAME, "roomId")
    _shift_first_room_name_field = (By.XPATH, "//div[2]/div/div/div/div/div/div/div")
    _shift_second_room_name_field = (By.XPATH, "//div[2]/div/div/div/div/div/div[2]/div")
    _shift_select_first_room_publish_checkbox = (By.NAME, "publishRoomId")
    _shift_select_second_room_publish_checkbox = (By.XPATH, "//div[2]/div[2]/div/div[4]/div/input")
    _add_daily_shift_button = (By.XPATH, "//div[@id='__blaze-root']/div[2]/div[2]/div/div/button")
    _add_daily_shift_name_value = "Daily Shift Abend"
    _add_daily_shift_internal_name_value = "Daily abend"
    _remove_first_daily_shift_button = (By.XPATH, "//td[6]/button")
    _daily_shift_activate_global_checkbox = (By.NAME, "selectedGlobalShifts")
    _daily_shift_activate_global_save_button = (By.XPATH, "//form/button")
    _daily_shift_first_global_name_field = (By.XPATH, "//div/label")
    _daily_shift_edit_first_button = (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/table/tbody/tr/td[1]/a")
    _first_shift_archive_button = (By.XPATH, "//td[6]/button[3]")
    _first_shift_internal_name_field = (By.CSS_SELECTOR, "td.internalName")
    _unarchive_shift_button = (By.XPATH, "//table[2]/tbody/tr/td[6]/button[3]")
    _expand_archived_shifts_button = (By.XPATH, "//div[2]/div/div/button[2]")
    _first_archived_shift_internal_name_field = (By.XPATH, "//table[2]/tbody/tr/td[2]")
    _tables_tab = (By.XPATH, "//div/ul/li[5]/a")
    _table_name_value = get_random_string(6)
    _table_name_field = (By.NAME, "tableName")
    _table_capacity_value = get_random_integer(2)
    _table_capacity_field = (By.NAME, "tableCapacity")
    _add_table_button = (By.XPATH, "//form/div/button")
    _first_table_name_field = (By.CSS_SELECTOR, "td.tableName")
    _first_table_capacity_field = (By.CSS_SELECTOR, "td.tableCapacity")
    _remove_first_table_button = (By.XPATH, "//td[3]/button[2]")
    _holidays_tab = (By.XPATH, "//div/ul/li[6]/a")
    _add_holiday_button = (By.XPATH, "//div[@id='__blaze-root']/div[2]/div[2]/div/div/button")
    _holiday_name_field = (By.NAME, "name")
    _holiday_name_value = get_random_string(7)
    _holiday_from_to_checkbox = (By.NAME, "hasRange")
    _holiday_start_date_value = str(datetime.date.today().day)+"."+str(datetime.date.today().month)+"."+str(datetime.date.today().year)
    _holiday_start_date_field = (By.NAME, "startDate")
    _holiday_end_date_value = str(datetime.date.today().day+1)+"."+str(datetime.date.today().month)+"."+str(datetime.date.today().year)
    _holiday_end_date_field = (By.NAME, "endDate")
    _holiday_information_value = get_random_string(5)+" "+get_random_string(6)+" "+get_random_string(7)
    _holiday_information_text_field = (By.XPATH, "//div[2]/div[3]/div[3]")
    _holiday_information_open_field = (By.CSS_SELECTOR, "html.bg-aleno body.modal-open div#__blaze-root div.wrap div.container-fluid.main-content.main-content-user-layout.slideMe div.row div.col-xs-12 div#holiday-add-modal.modal.fade.in div.modal-dialog div.modal-content div.modal-body form#addHolidays.form.restaurantSettings div.form-body div.multi-locales-field div.js-locale-input.js-locale-item-de-CH.visible div.form-group.form-group-summernote div.form-container div.htmleditor-textarea-imitate.js-htmleditor-textarea-imitate")
    _holiday_information_close_field = (By.XPATH, "//button[@title='Close']")
    _add_holiday_submit = (By.XPATH, "//div[2]/div/button")
    _first_added_holiday_name_field = (By.XPATH, "//td/a")
    _first_added_holiday_from_field = (By.CSS_SELECTOR, "td.startDate")
    _first_added_holiday_to_field = (By.CSS_SELECTOR, "td.endDate")
    _first_added_holiday_information_field = (By.CSS_SELECTOR, "td.message")
    _edit_holiday_name_value = get_random_string(8)
    _edit_holiday_name_field = (By.XPATH, "//div[2]/div/div[2]/form/div/div/div/input")
    _edit_holiday_start_date_value = str(datetime.date.today().day-1)+"."+str(datetime.date.today().month)+"."+str(datetime.date.today().year)
    _edit_holiday_start_date_field = (By.XPATH, "//div[2]/div/div[2]/form/div/div[3]/div/input")
    _edit_holiday_end_date_value = str(datetime.date.today().day)+"."+str(datetime.date.today().month)+"."+str(datetime.date.today().year)
    _first_day_next_month = "1."+str(datetime.date.today().month+1)+"."+str(datetime.date.today().year)
    _last_day_previous_month = "29."+str(datetime.date.today().month-1)+"."+str(datetime.date.today().year)
    _edit_holiday_end_date_field = (By.XPATH, "//form[@id='editHolidays']/div/div[4]/div/input")
    _edit_holiday_information_value = get_random_string(6)+" "+get_random_string(5)+" "+get_random_string(3)
    _edit_holiday_information_text_field = (By.XPATH, "//form[@id='editHolidays']/div/div[5]/div[2]/div/div/div[2]/div[3]/div[3]")
    _edit_holiday_information_open_field = (By.XPATH, "//form[@id='editHolidays']/div/div[5]/div[2]/div/div/div")
    _edit_holiday_information_close_field = (By.XPATH, "//form[@id='editHolidays']/div/div[5]/div[2]/div/div/button")
    _edit_holiday_submit = (By.XPATH, "//form[@id='editHolidays']/div[2]/div/button")
    _remove_first_added_holiday_button = (By.XPATH, "//td[5]/button")
    _coustomizations_tab = (By.XPATH, "//div/ul/li[10]/a")
    _percentage_of_capacity_labeled_as_confirmed_checkbox = (By.XPATH, "//form/div/div/input")
    _percentage_of_capacity_labeled_as_confirmed_field = (By.NAME, "serviceRole80")
    _percentage_of_capacity_labeled_as_confirmed_value = str(randint(1,99))
    _booking_in_advance_field = (By.NAME, "daysInAdvance")
    _booking_in_advance_value = str(randint(1,200))
    _save_coustomizations_tab = (By.XPATH, "//div[2]/div/button")

    def __init__(self, driver):
        super(RestaurantSettingsPage, self).__init__(driver, self._title)

    def get_restaurant_info(self):
        self.restaurant_info_last_name = self.get_value(self._last_name_field, "Trying to get the value from the restaurant last name field on the restaurant settings page was unsuccessful")
        self.restaurant_info_address = self.get_value(self._address_field, "Trying to get the value from the restaurant address field on the restaurant settings page was unsuccessful")
        self.restaurant_info_zip = self.get_value(self._zip_code_field, "Trying to get the value from the restaurant zip code field on the restaurant settings page was unsuccessful")
        self.restaurant_info_city = self.get_value(self._city_field, "Trying to get the value from the restaurant city field on the restaurant settings page was unsuccessful")
        self.restaurant_info_country = self.get_value(self._country_field, "Trying to get the value from the restaurant country field on the restaurant settings page was unsuccessful")
        self.restaurant_info_email = self.get_value(self._email_field, "Trying to get the value from the restaurant email field on the restaurant settings page was unsuccessful")
        self.restaurant_info_senders_email = self.get_value(self._senders_email_field, "Trying to get the value from the senders email field on the restaurant settings page was unsuccessful")
        self.restaurant_info_msgIn_email = self.get_value(self._msgIn_email_field, "Trying to get the value from the msgIn email field on the restaurant settings page was unsuccessful")
        self.restaurant_info_website = self.get_value(self._website_field, "Trying to get the value from the restaurant website field on the restaurant settings page was unsuccessful")
        self.restaurant_info_facebook = self.get_value(self._facebook_field, "Trying to get the value from the restaurant facebook field on the restaurant settings page was unsuccessful")
        self.restaurant_info_fan_page = self.get_value(self._fan_page_url_field, "Trying to get the value from the restaurant fan page url field on the restaurant settings page was unsuccessful")
        self.restaurant_info_trip_advisor = self.get_value(self._trip_advisor_field, "Trying to get the value from the trip advisor field on the restaurant settings page was unsuccessful")
        self.restaurant_info_google = self.get_value(self._google_field, "Trying to get the value from the restaurant google field on the restaurant settings page was unsuccessful")
        self.restaurant_info_yelp = self.get_value(self._yelp_field, "Trying to get the value from the restaurant yelp field on the restaurant settings page was unsuccessful")
        self.restaurant_info_phone = self.get_value(self._phone_field, "Trying to get the value from the restaurant phone field on the restaurant settings page was unsuccessful")
        self.restaurant_info_image_url = self.get_value(self._image_url_field, "Trying to get the value from the restaurant image url field on the restaurant settings page was unsuccessful")

    def open_rooms_tab(self):
        self.click(self._rooms_tab, "Rooms tab cannot be clicked or wasn't found on the restaurant settings page")

    def add_two_rooms(self):
        # self.click(self._add_room_en_button)
        self.clear_field_and_send_keys(self._add_room_name_value1, self._add_room_name_field, "The field to enter room name to add room on restaurant room settings page didn't show")
        self.click(self._add_room_submit, "Button to submit adding room cannot be clicked or wasn't found on the restaurant settings page")
        sleep(3)
        self.clear_field_and_send_keys(self._add_room_name_value2, self._add_room_name_field, "The field to enter room name to add room on restaurant room settings page didn't show")
        self.click(self._add_room_submit, "Button to submit adding room cannot be clicked or wasn't found on the restaurant settings page")
        self.clear_field_and_send_keys(self._add_room_capacity_value, self._add_room_capacity_field1, "The first room field to enter room capacity on restaurant room settings page didn't show")
        self.clear_field_and_send_keys(self._add_room_capacity_value, self._add_room_capacity_field2, "The second room field to enter room capacity on restaurant room settings page didn't show")
        self.clear_field_and_send_keys(self._add_room_bookable_value, self._add_room_bookable_field1, "The first room field to enter room bookable value on restaurant room settings page didn't show")
        self.clear_field_and_send_keys(self._add_room_bookable_value, self._add_room_bookable_field2, "The second room field to enter room bookable value on restaurant room settings page didn't show")
        self.clear_field_and_send_keys(self._add_room_order_value1, self._add_room_order_field1, "The first room field to enter room order on restaurant room settings page didn't show")
        self.clear_field_and_send_keys(self._add_room_order_value2, self._add_room_order_field2, "The second room field to enter room order on restaurant room settings page didn't show")

    def remove_added_rooms(self):
        self.click(self._add_room_remove_first, "Button to remove first added room cannot be clicked or wasn't found on the restaurant settings page")
        self.accept_alert()
        sleep(3)
        self.click(self._add_room_remove_first, "Button to remove first added room cannot be clicked or wasn't found on the restaurant settings page")
        self.accept_alert()
        sleep(3)

    def open_shift_tab(self):
        self.click(self._shift_tab, "Shifts tab cannot be clicked or wasn't found on the restaurant settings page")
        sleep(2)

    def add_shift_first_accordeon(self):
        self.click(self._add_shift_button, "Add shift button cannot be clicked or wasn't found on the restaurant shifts settings page")
        self.clear_field_and_send_keys(self._shift_name_value, self._shift_name_field, "The shift name field on add shift page didn't show")
        self.clear_field_and_send_keys(self._shift_internal_name_value, self._shift_internal_name_field, "The shift internal name field on add shift page didn't show")
        self.clear_field_and_send_keys(self._shift_start_date_value, self._shift_start_date_field, "The shift start date field on add shift page didn't show")
        self.clear_field_and_send_keys(self._shift_service_start_value, self._shift_service_start_field, "The shift service start field on add shift page didn't show")
        self.clear_field_and_send_keys(self._shift_service_end_value, self._shift_service_end_field, "The shift service end field on add shift page didn't show")

    def add_shift_second_accordeon(self):
        self.click(self._shift_second_accordeon_menu, "While adding shift second accordeon tab cannot be clicked or wasn't found on the page")
        self.click(self._shift_reservation_requirements_checkbox), "Shift reservation requirements checkbox cannot be clicked or wasn't found on the register shift page"
        sleep(2)
        self.clear_field_and_send_keys(self._shift_capacity_value, self._shift_capacity_field, "The shift capacity field on add shift page didn't show")
        self.clear_field_and_send_keys(self._shift_reservations_confirmed_value, self._shift_reservations_confirmed_field, "The shift reservations confirmed field on add shift page didn't show")
        self.clear_field_and_send_keys(self._shift_buffer_value, self._shift_buffer_field, "The shift buffer field on add shift page didn't show")
        self.clear_field_and_send_keys(self._shift_daily_online_deadline_value, self._shift_daily_online_deadline_field, "The shift daily online deadline field on add shift page didn't show")
        self.clear_field_and_send_keys(self._shift_kitchen_start_value, self._shift_kitchen_start_field, "The shift kitchen start field on add shift page didn't show")
        self.clear_field_and_send_keys(self._shift_kitchen_end_value, self._shift_kitchen_end_field, "The shift kitchen end field on add shift page didn't show")
        self.clear_field_and_send_keys(self._shift_duration_of_reservation_value, self._shift_duration_of_reservation_field, "The shift duration of reservation field on add shift page didn't show")
        self.clear_field_and_send_keys(self._shift_timeslot_capacity_value, self._shift_timeslot_capacity_field, "The shift timeslot capacity field on add shift page didn't show")
        self.clear_field_and_send_keys(self._shift_minimum_guests_value, self._shift_minimum_guests_field, "The shift minimum guests field on add shift page didn't show")
        self.clear_field_and_send_keys(self._shift_maximum_guests_value, self._shift_maximum_guests_field, "The shift maximum guests field on add shift page didn't show")

    def save_shift(self):
        self.click(self._shift_save_button, "Save shift button cannot be clicked or wasn't found on the register shift page")

    def open_first_shift_details(self):
        self.click(self._added_shift_show_copies_button, "First shift details button (show copies) cannot be clicked or wasn't found on the restaurant shifts settings page")

    def first_shift_get_values(self):
        self.added_shift_name = self.get_value(self._added_shift_name_field, "Trying to get the value from shift name field on the first shift show copies page was unsuccessful")
        self.added_shift_internal_name = self.get_value(self._added_shift_internal_name_field, "Trying to get the value from shift internal name field on the first shift show copies page was unsuccessful")
        self.added_shift_capacity = self.get_value(self._shift_capacity_field, "Trying to get the value from shift capacity field on the first shift show copies page was unsuccessful")
        self.added_shift_buffer = self.get_value(self._shift_buffer_field, "Trying to get the value from shift buffer field on the first shift show copies page was unsuccessful")
        self.get_driver().execute_script("window.scrollTo(1100, 0);")
        self.added_shift_daily_deadlinie = self.get_value(self._shift_daily_online_deadline_field, "Trying to get the value from shift daily online deadline field on the first shift show copies page was unsuccessful")
        self.added_shift_kitchen_start = self.get_value(self._shift_kitchen_start_field, "Trying to get the value from shift kitchen start field on the first shift show copies page was unsuccessful")
        self.added_shift_kitchen_end = self.get_value(self._shift_kitchen_end_field, "Trying to get the value from shift kitchen end field on the first shift show copies page was unsuccessful")
        self.get_driver().execute_script("window.scrollTo(2000, 0);")
        self.added_shift_timeslot_capacity = self.get_value(self._shift_timeslot_capacity_field, "Trying to get the value from shift timeslot capacity field on the first shift show copies page was unsuccessful")
        self.added_shift_reservations_confirmed = self.get_value(self._shift_reservations_confirmed_field, "Trying to get the value from shift reservations confirmed field on the first shift show copies page was unsuccessful")
        self.added_shift_minimum_guests = self.get_value(self._shift_minimum_guests_field, "Trying to get the value from shift minimum guests field on the first shift show copies page was unsuccessful")
        self.added_shift_maximum_guests = self.get_value(self._shift_maximum_guests_field, "Trying to get the value from shift maximum guests field on the first shift show copies page was unsuccessful")

    def remove_first_shift(self):
        self.click(self._remove_added_shift_button, "Remove first shift button cannot be clicked or wasn't found on the restaurant shifts settings page")
        self.accept_alert()

    def add_1_room_to_shift(self):
        self.click(self._shift_third_accordeon_menu, "While adding shift - the third accordeon cannot be clicked or wasn't found on the page")
        self.first_room_name = self.get_text(self._shift_first_room_name_field)
        self.click(self._shift_select_first_room_checkbox, "While adding shift - in the third accordeon the select first room checkbox cannot be clicked or wasn't found on the page")

    def add_2_rooms_to_shift_publish(self):
        self.click(self._shift_third_accordeon_menu, "While adding shift - the third accordeon cannot be clicked or wasn't found on the page")
        self.first_room_name = self.get_text(self._shift_first_room_name_field)
        self.second_room_name = self.get_text(self._shift_second_room_name_field)
        self.click(self._shift_select_first_room_publish_checkbox, "While adding shift - in the third accordeon the first room \"Publish\" checkbox cannot be clicked or wasn't found on the page")
        self.click(self._shift_select_second_room_publish_checkbox, "While adding shift - in the third accordeon the second room \"Publish\" checkbox cannot be clicked or wasn't found on the page")

    def add_daily_shift_click_button(self):
        self.click(self._add_daily_shift_button, "The button to add daily shift cannot be clicked or wasn't found on the daily shifts page")

    def add_shift_daily_first_accordeon(self):
        self.clear_field_and_send_keys(self._add_daily_shift_name_value, self._shift_name_field, "The shift name field on add daily shift page didn't show")
        self.clear_field_and_send_keys(self._add_daily_shift_internal_name_value, self._shift_internal_name_field, "The shift internal name field on add daily shift page didn't show")
        self.clear_field_and_send_keys(self._shift_service_start_value, self._shift_service_start_field, "The shift service start field on add shift page didn't show")
        self.clear_field_and_send_keys(self._shift_service_end_value, self._shift_service_end_field, "The shift service end field on add shift page didn't show")

    def remove_first_daily_shift(self):
        self.click(self._remove_first_daily_shift_button, "The remove first daily shift button cannot be clicked or isn't present on the daily shifts page")
        self.accept_alert()

    def daily_shift_activate_first_global(self):
        self.click(self._daily_shift_activate_global_checkbox, "The first global shift checkbox in the daily shifts menu cannot be clicked or wasn't visible on the daily shifts page")
        self.click(self._daily_shift_activate_global_save_button, "The save global shift button in the daily shifts menu cannot be clicked or wasn't visible on the daily shifts page")

    def get_first_global_shift_name(self):
        self.first_global_shift_name = self.get_text(self._daily_shift_first_global_name_field)

    def get_first_active_shift_internal_name(self):
        self.first_active_shift_internal_name = self.get_text(self._first_shift_internal_name_field)

    def edit_first_daily_shift(self):
        self.condition_click(self._daily_shift_edit_first_button, "The edit first daily shift button cannot be clicked or wasn't visible on the daily shift page")

    def archive_first_shift(self):
        self.click(self._first_shift_archive_button, "First shift Archive button on the restaurant shifts settings page cannot be clicked or isn't found on the page")

    def get_first_shift_internal_name(self):
        self._first_shift_internal_name = self.get_text(self._first_shift_internal_name_field)

    def expand_archived_shifts(self):
        self.click(self._expand_archived_shifts_button, "Expand archived shifts button cannot be clicked or isn't found on the restaurant shifts settings page")

    def unachive_shift(self):
        self.click(self._unarchive_shift_button, "Unarchive first shift button cannot be clicked or wasn't found on the restaurant shifts settings page")

    def open_tables_tab(self):
        self.click(self._tables_tab, "The tables tab in the restaurant settings cannot be clicked or wasn't found on the page")

    def add_table(self):
        self.clear_field_and_send_keys(self._table_name_value, self._table_name_field, "The table name field on add table page didn't show")
        self.clear_field_and_send_keys(self._table_capacity_value, self._table_capacity_field, "The table capacity field on add table page didn't show")
        self.click(self._add_table_button, "The add table button cannot be clicked or wasn't found on the add table page")

    def remove_first_table(self):
        self.click(self._remove_first_table_button, "The remove first table button cannot be clicked or wasn't found on the add table page")
        self.accept_alert()

    def open_holidays_tab(self):
        self.click(self._holidays_tab, "Holidays tab cannot be clicked or wasn't found on the restaurant settings page")
        sleep(2)

    def add_holiday(self):
        self.click(self._add_holiday_button, "Add holiday button cannot be clicked or wasn't found on the holidays tab in restaurant settings")
        sleep(2)
        self.clear_field_and_send_keys(self._holiday_name_value, self._holiday_name_field, "The holiday name field on add holiday page didn't show")
        self.click(self._holiday_from_to_checkbox, "While adding holiday, the \"From\" checkbox cannot be clicked or wasn't found on the page")
        self.clear_field_and_send_keys(self._holiday_start_date_value, self._holiday_start_date_field, "The holiday start date field on add holiday page didn't show")
        if (datetime.date.today().day)==29 and (datetime.date.today().month)==2:
            self.clear_field_and_send_keys(self._first_day_next_month, self._holiday_end_date_field, "The holiday end date field on add holiday page didn't show")
        elif (datetime.date.today().day)==30 or (datetime.date.today().day)==31:
            self.clear_field_and_send_keys(self._first_day_next_month, self._holiday_end_date_field, "The holiday end date field on add holiday page didn't show")
        else:
            self.clear_field_and_send_keys(self._holiday_end_date_value, self._holiday_end_date_field, "The holiday end date field on add holiday page didn't show")
        self._holiday_end_date_inserted = self.get_text(self._holiday_end_date_field)
        self.click(self._holiday_name_field, "While adding holiday, the \"Holiday name\" field cannot be clicked or wasn't found on the page")
        self.click(self._holiday_information_open_field, "While adding holiday, the attempt to open \"Holiday information\" field to enter data to it wasn't successful")
        self.clear_field_and_send_keys(self._holiday_information_value, self._holiday_information_text_field, "The holiday information text field on add holiday page didn't show")
        self.click(self._holiday_information_close_field, "While adding holiday, the attempt to close \"Holiday information\" field after entering data to it wasn't successful")
        self.click(self._add_holiday_submit, "While adding holiday, the attempt to click \"Submit\" button wasn't successful")

    def edit_holiday(self):
        self.condition_click(self._first_added_holiday_name_field, "The first holiday name field on the holidays tab cannot be clicked or wasn't found on the page, so added holiday cannot be edited")
        sleep(2)
        self.clear_field_and_send_keys(self._edit_holiday_name_value, self._edit_holiday_name_field, "The holiday edit name field on edit holiday page didn't show")
        if (datetime.date.today().day)==1:
            self.clear_field_and_send_keys(self._last_day_previous_month, self._edit_holiday_start_date_field, "The holiday start date field on edit holiday page didn't show")
        else:
            self.clear_field_and_send_keys(self._edit_holiday_start_date_value, self._edit_holiday_start_date_field, "The holiday start date field on edit holiday page didn't show")
        self._edit_holiday_start_date_inserted = self.get_text(self._edit_holiday_start_date_field)
        self.clear_field_and_send_keys(self._edit_holiday_end_date_value, self._edit_holiday_end_date_field, "The holiday end date field on edit holiday page didn't show")
        self.click(self._edit_holiday_name_field, "While editing holiday, the \"Holiday name\" field cannot be clicked or wasn't found on the page")
        self.click(self._edit_holiday_information_open_field, "While editing holiday, the attempt to open \"Holiday information\" field to enter data to it wasn't successful")
        self.clear_field_and_send_keys(self._edit_holiday_information_value, self._edit_holiday_information_text_field, "The holiday information field on edit holiday page didn't show")
        self.click(self._edit_holiday_information_close_field,"While editing holiday, the attempt to close \"Holiday information\" field after entering data to it wasn't successful")
        self.click(self._edit_holiday_submit, "While editing holiday, the \"Submit\" button cannot be clicked or wasn't found on the page")

    def remove_added_holiday(self):
        self.condition_click(self._remove_first_added_holiday_button, "The remove first added holiday button on holidays tab cannot be clicked or wasn't found on the page")
        self.accept_alert()

    def open_coustomizations_tab(self):
        self.click(self._coustomizations_tab, "The coustomization tab in restaurant settings page cannot be clicked or wasn't found on the page")
        sleep(2)

    def click_percentage_of_capacity_checkbox(self):
        self.click(self._percentage_of_capacity_labeled_as_confirmed_checkbox, "The percentage of capacity labeled as confirmed checkbox cannot be clicked or wasn't found on the restaurant coustomizations settings page")

    def edit_coustomization_tab(self):
        self.clear_field_and_send_keys(self._percentage_of_capacity_labeled_as_confirmed_value, self._percentage_of_capacity_labeled_as_confirmed_field, "The percentage of capacity labeled as confirmed field on restaurant coustomization settings page didn't show")
        self.clear_field_and_send_keys(self._booking_in_advance_value, self._booking_in_advance_field, "The booking in advance field on restaurant coustomization settings page didn't show")
        self.click(self._save_coustomizations_tab, "The save coustomizations tab settings button cannot be clicked or wasn't found on the page")

    def get_vaules_coustomization_tab(self):
        self._percentage_of_capacity_labeled_as_confirmed_saved_value = self.get_value(self._percentage_of_capacity_labeled_as_confirmed_field, "The attempt to get value of the precentage of capacity labeled as confirmed field in the coustomizations tab in restaurant settings wasn't successful")
        self._booking_in_advance_saved_value = self.get_value(self._booking_in_advance_field, "The attempt to get value of the booking in advance field in the coustomizations tab in restaurant settings wasn't successful")