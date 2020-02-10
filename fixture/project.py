# -*- coding: utf-8 -*-
import time
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url+"/manage_proj_page.php")
        time.sleep(1)

    projects_cache = None

    def get_projects_list_from_table(self):
        if self.projects_cache is None:
            wd = self.app.wd
            self.projects_cache = []
            for row in wd.find_elements_by_xpath("//div[2]/table/tbody/tr"):
                cells = row.find_elements_by_tag_name("td")
                link = row.find_element_by_css_selector("a").get_attribute('href')
                id = link[link.find("=") + 1:]
                name = cells[0].text
                status = cells[1].text
                viewstatus = cells[3].text
                description = cells[4].text
                scanned_project = Project(id=id, name=name, status=status, viewstatus=viewstatus,
                                          description=description)
                self.projects_cache.append(scanned_project)
        return list(self.projects_cache)

    def create(self, proj_to_add):
        wd = self.app.wd
        wd.find_element_by_xpath("//*/text()[normalize-space(.)='Create New Project']/parent::*").click()
        self.app.change_field_value("name", proj_to_add.name)
        self.app.change_field_value("description", proj_to_add.description)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.projects_cache = None
        time.sleep(2)

    def delete(self, proj_to_del):
        wd = self.app.wd
        pr_id = proj_to_del.id
        wd.find_element_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=%s')]" % pr_id).click()
        time.sleep(1)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        time.sleep(1)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        time.sleep(1)
        self.projects_cache = None
