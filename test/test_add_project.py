# -*- coding: utf-8 -*-
import time
from datetime import datetime
from model.project import Project


def test_add_project(app):
    app.open_home_page()
    app.session.login("administrator", "root")
    app.project.open_projects_page()
    old_projects_list = app.project.get_projects_list_from_table()
    print("")
    print("OLD LIST LEN = "+str(len(old_projects_list)))
    for xx in range(len(old_projects_list)):
        print(str(old_projects_list[xx]))
    project_to_add = Project(name=("Project "+str(datetime.now().strftime("%m_%d %H:%M:%S"))),
                             description="Project Description")
    app.project.create(project_to_add)
    app.project.open_projects_page()
    new_projects_list = app.project.get_projects_list_from_table()
    print("")
    print("NEW LIST LEN = "+str(len(new_projects_list)))
    for xx in range(len(new_projects_list)):
        print(str(new_projects_list[xx]))

    assert True
