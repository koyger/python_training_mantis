# -*- coding: utf-8 -*-
import os.path
import ftputil


def put_file_via_ftp(host, username, password):
    with ftputil.FTPHost(host, username, password) as remote:
        print("LOOKING FOR FILES/FOLDERS")
        list = remote.listdir(remote.curdir)
        for item in list:
            print("item : "+item)
        remote.chdir('mantisbt-2.23.0/config')
        print('CHDIR to '+remote.getcwd())
        remote.upload("../resources/config_inc.php", "TEST_config_inc_TEST.php")


put_file_via_ftp("localhost", "mantis", "calella1212")
print("PUT TEST_config_inc_TEST.php DONE")
