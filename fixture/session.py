# -*- coding: utf-8 -*-
import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_css_selector("input.width-40.pull-right.btn.btn-success.btn-inverse.bigger-110").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_css_selector("input.width-40.pull-right.btn.btn-success.btn-inverse.bigger-110").click()

    # def logout(self):
    #     wd = self.app.wd
    #     wd.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        self.app.open_home_page()
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//td[contains(text(),'Logged')]")) > 0

    def ensure_login(self, username, password):
        self.app.open_home_page()
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in_as(self, username):
        scanned_name = self.get_logged_user()
        return scanned_name == username

    def get_logged_user(self):
        wd = self.app.wd
        logged_name = wd.find_element_by_css_selector("ul.breadcrumb > li > a").text
        return logged_name

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='navbar-container']/div[2]/ul/li[3]/a/i[2]").click()
        wd.find_element_by_xpath("//div[@id='navbar-container']/div[2]/ul/li[3]/ul/li[4]/a/i").click()
        time.sleep(1)

