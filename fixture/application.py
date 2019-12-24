# -*- coding: utf-8 -*-
import re
from selenium import webdriver
from fixture.session import SessionHelper


class Application:

    def __init__(self, browser, base_url):
        # self.wd = webdriver.Chrome()
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        self.base_url = base_url
        self.session = SessionHelper(self)

    def is_valid(self):
        try:
            # it is a check that session is alive
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath(
                "//a[contains(text(),'Last name')]")) > 0):
            self.wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def change_field_value(app, field_name, text):
        wd = app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def clear(self, some_text):
        return re.sub("[() -]", "", some_text)
