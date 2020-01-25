import unittest
import pdb
from time import sleep
from src.utility.appiumdriver import Driver
from src.locators.country_selection_screen_locators import CountrySelectionLocators


class CountryTest(Driver):

    def __init__(self, driver):
        super().__init__(driver)

    def test_select_chile(self):
        self.driver.find_element_by_xpath(CountrySelectionLocators.chile)
        # pdb.set_trace()

    def test_test_select_argentina(self):
        self.driver.find_element_by_xpath(CountrySelectionLocators.argentina)
