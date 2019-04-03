from selenium.webdriver.support.select import Select
from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def check_if_contacts_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_link_text("Logout")) > 0 and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.check_if_contacts_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("%s" % contact.firstname)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("%s" % contact.lastname)
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
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def update_value(self, contact_field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(contact_field_name).click()
            wd.find_element_by_name(contact_field_name).clear()
            wd.find_element_by_name(contact_field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.update_value("firstname", contact.firstname)
        self.update_value("email", contact.email)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.check_if_contacts_page()
        self.select_contact_by_index(index)
        # submit edition
        wd.find_elements_by_css_selector("img[alt='Edit']")[index].click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit contact update
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.check_if_contacts_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # close dialog
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def return_to_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.check_if_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.check_if_contacts_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.check_if_contacts_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.check_if_contacts_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text)
        if homephone:
            homephone = homephone.group(1)

        mobilephone = re.search("M: (.*)", text)
        if mobilephone:
            mobilephone = mobilephone.group(1)

        workphone = re.search("W: (.*)", text)
        if workphone:
            workphone = workphone.group(1)

        secondaryphone = re.search("P: (.*)", text)
        if secondaryphone:
            secondaryphone = secondaryphone.group(1)

        # homephone = re.search("H: (.*)", text).group(1)
        # mobilephone = re.search("M: (.*)", text).group(1)
        # workphone = re.search("W: (.*)", text).group(1)
        # secondaryphone = re.search("P: (.*)", text).group(1)

        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)







