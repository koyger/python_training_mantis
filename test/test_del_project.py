# -*- coding: utf-8 -*-
import random
from datetime import datetime
from model.project import Project


def test_del_project(app):
    app.project.open_projects_page()
    old_projects_list = app.project.get_projects_list_from_table()
    if len(old_projects_list) == 0:
        project_to_add = Project(name=("FIRST Project " + str(datetime.now().strftime("%m_%d %H:%M:%S"))),
                                 description="FIRST Project Description")
        app.project.create(project_to_add)
    old_projects_list = app.project.get_projects_list_from_table()
    proj_to_del = random.choice(old_projects_list)
    app.project.delete(proj_to_del)
    new_projects_list = app.project.get_projects_list_from_table()
    assert len(old_projects_list) == len(new_projects_list)+1
    old_projects_list.remove(proj_to_del)
    assert sorted(old_projects_list, key=Project.id_or_max) == sorted(new_projects_list, key=Project.id_or_max)
