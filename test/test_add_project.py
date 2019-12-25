# -*- coding: utf-8 -*-
from datetime import datetime
from model.project import Project


def test_add_project(app):
    app.project.open_projects_page()
    old_projects_list = app.project.get_projects_list_from_table()
    project_to_add = Project(name=("Project "+str(datetime.now().strftime("%m_%d %H:%M:%S"))),
                             description="Project Description")
    app.project.create(project_to_add)
    app.project.open_projects_page()
    new_projects_list = app.project.get_projects_list_from_table()
    assert len(old_projects_list) == len(new_projects_list)-1
    old_projects_list.append(project_to_add)
    assert sorted(old_projects_list, key=Project.id_or_max) == sorted(new_projects_list, key=Project.id_or_max)
