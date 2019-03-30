from selenium.webdriver.support.select import Select

from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def check_if_contacts_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_link_text("Logout")) > 0 and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        self.check_if_contacts_page()
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
        self.update_value("firstname", contact.contactname)
        self.update_value("email", contact.email)

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.check_if_contacts_page()
        self.select_first_contact()
        # submit edition
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit contact update
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.check_if_contacts_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # close dialog
        wd.switch_to.alert.accept()

    def return_to_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.check_if_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.check_if_contacts_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            text = element.find_element_by_xpath("//td[2]").text
            text2 = element.find_element_by_xpath("//td[3]").text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(contactsurname=text, contactname=text2, id=id))
        return contacts
