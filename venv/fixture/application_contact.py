from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.session import SessionHelper


class ApplicationContact:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session_contact = SessionHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy_contact(self):
        self.wd.quit()