# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import By

from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    projects_cache = None

    def get_projects_list_from_table(self):
        if self.projects_cache is None:
            wd = self.app.wd
            self.open_projects_page()
            self.projects_cache = []
            for row in wd.find_elements_by_xpath("//table[3]/tbody/tr")[2:]:  # first two rows are not Projects
                cells = row.find_elements_by_tag_name("td")
                link = row.find_element_by_css_selector("a").get_attribute('href')
                id = link[link.find("=") + 1:]
                name = cells[0].text
                status = cells[1].text
                enabled = cells[2].text
                viewstatus = cells[3].text
                description = cells[4].text
                scanned_project = Project(id=id, name=name, status=status, enabled=enabled, viewstatus=viewstatus,
                                          description=description)
                self.projects_cache.append(scanned_project)
        return list(self.projects_cache)