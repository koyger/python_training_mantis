from suds.client import Client
from suds import WebFault
from fixture.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-2.23.0/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def projects_list(self, username, password):
        client = Client("http://localhost/mantisbt-2.23.0/api/soap/mantisconnect.php?wsdl")
        pr_list = []
        try:
            pr_soap_list = client.service.mc_projects_get_user_accessible(username, password)
            for n in range(len(pr_soap_list)):
                scanned_project = Project(id=pr_soap_list[n]['id'], name=pr_soap_list[n]['name'],
                                          description=pr_soap_list[n]['description'])
                pr_list.append(scanned_project)
            return pr_list
        except WebFault:
            return pr_list
