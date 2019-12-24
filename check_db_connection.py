from fixture.db import DbFixture
from fixture.orm import ORMFixture
import pymysql.cursors
from model.group import Group

db = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    l = db.get_contacts_in_group(Group(id="371"))

    for one in l:
        print(one)
    print(len(l))
finally:
    pass
    # db.destroy()


