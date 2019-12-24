# -*- coding: utf-8 -*-
from model.project import Project


def test_add_project(app):
    app.open_home_page()
    app.session.login("administrator", "root")
    old_projects_list = app.project.get_projects_list_from_table()
    print(old_projects_list)
    project_to_add = Project()
    assert True
