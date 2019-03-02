# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

from contact import Contact


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd, Contact(contactname="Adam", contactsurname="Nowak", contactnickname="Nowy", title="manager", company="INext", address=u"Kościuszki St, Wrocław", homephone="48333444555", mobilephone="48888777666", email="nowak@go.pl", byear="1977"))
        self.return_to_contacts_page(wd)
        self.logout(wd)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def create_contact(self, wd, contact):
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("%s" % contact.contactname)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("%s" % contact.contactsurname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("%s" % contact.contactnickname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("%s" % contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("%s" % contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(u"%s" % contact.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("+%s" % contact.homephone)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("+%s" % contact.mobilephone)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("%s" % contact.email)
        Select(wd.find_element_by_name("bday")).select_by_visible_text("15")
        wd.find_element_by_xpath("//option[@value='15']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("October")
        wd.find_element_by_xpath("//option[@value='October']").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("%s" % contact.byear)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def return_to_contacts_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
