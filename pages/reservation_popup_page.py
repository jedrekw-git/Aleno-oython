# coding=utf-8
from selenium.webdriver.common.by import By
from pages.base import BasePage
from utils.utils import *
from random import randint
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ReservationPopupPage(BasePage):
    _title = "Reservation Popup Page"

    _other_button = (By.XPATH, "/html/body/div/div/div[4]/button")
    _first_shift_button = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div[2]/table/tr[1]/th[1]/span[2]/span[1]")

    def __init__(self, driver):
        super(ReservationPopupPage, self).__init__(driver, self._title)

    def click_other_button(self):
        self.click(self._other_button)

    def click_first_shift(self):
        self.click(self._first_shift_button)







