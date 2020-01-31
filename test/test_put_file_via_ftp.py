# -*- coding: utf-8 -*-
import os.path
import ftputil


def test_put_file_via_ftp(host, username, password):
    with ftputil.FTPHost(host, username, password) as remote:
        print("")
        list = remote.listdir(remote.curdir)
        for item in list:
            print("item : "+item)
        remote.chdir('mantisbt-2.23.0')
        print('mantisbt-2.23.0')
        list = remote.listdir(remote.curdir)
        for item in list:
            print("item : "+item)

        # remote.upload("/home/koyger/PycharmProjects/python_training_mantis/resources/config_inc.php", path_for_upload)


test_put_file_via_ftp("localhost", "mantis", "calella1212")
print("PUT FILE DONE")