import re
from sys import maxsize


class Project:

    def __init__(self, id=None, name=None, status=None, enabled = None, viewstatus=None, description=None):
        self.id = id
        self.name = name
        self.status = status
        self.enabled = enabled
        self.viewstatus = viewstatus
        self.description = description

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.name, self.status, self.enabled, self.viewstatus, self.description)

    def __eq__(self, other):
        s_name = self.clear(self.name)
        o_name = self.clear(other.name)
        return (self.id is None or other.id is None or self.id == other.id) and s_name == o_name

    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize


    @staticmethod
    def clear(s):
        return re.sub("[() -]", "", s)