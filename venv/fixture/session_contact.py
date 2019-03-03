
class SessionHelper:
    def __init__(self, app_contact):
        self.app_contact = app_contact

    def login(self, username, password):
        wd = self.app_contact.wd
        self.app_contact.open_home_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app_contact.wd
        wd.find_element_by_link_text("Logout").click()