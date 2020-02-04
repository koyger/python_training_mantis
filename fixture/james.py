from telnetlib import Telnet
class JamesHelper:

    def __init__(self, app):
        self.app = app

    def ensure_user_exists(self, username, password):
        session = JamesHelper.Session("localhost", 4555, "root", "root")
        if session.is_user_registered(username):
            session.reset_password(username, password)
        else:
            session.create_user(username, password)
        session.quit()

    class Session:

        def __init__(self, host, port, mail_user, mail_pass):
            self.telnet = Telnet(host, port, 5)
            self.read_until("Login id:")
            self.write(mail_user + "\n")
            self.read_until("Password:")
            self.write(mail_pass + "\n")
            self.read_until("Welcome root. HELP for a list of commands")

        def read_until(self, text):
            self.telnet.read_until(text.encode('ascii'), 5)

        def write(self, text):
            self.telnet.write(text.encode('ascii'))

        def is_user_registered(self, username):
            self.write("verify %s" % username + "\n")
            res = self.telnet.expect([b"exists", b"does not exist"])
            return res[0] == 0


        def create_user(self, username, password):
            self.write("adduser %s %s" % (username, password) + "\n")
            self.read_until("User %s added" % username)


        def reset_password(self, username, password):
            self.write("setpassword %s %s" % (username, password) + "\n")
            self.read_until("Password for %s reset" % username)

        def quit(self):
            self.write("quit\n")


