# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.james import JamesHelper
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper
from fixture.soap import SoapHelper


class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        self.config = config
        self.base_url = config['web']['baseUrl']
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.james = JamesHelper(self)
        self.mail = MailHelper(self)
        self.signup = SignupHelper(self)
        self.soap = SoapHelper(self)

    def is_valid(self):
        try:
            # it is a check that session is alive
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        self.wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def change_field_value(app, field_name, text):
        wd = app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

