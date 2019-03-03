# -*- coding: utf-8 -*-
import pytest
from fixture.application_contact import ApplicationContact
from model.contact import Contact


@pytest.fixture
def app_contact(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy_contact)
    return fixture

def test_add_contact(app_contact):
    app_contact.open_home_page()
    app_contact.session_contact.login(username="admin", password="secret")
    app_contact.contact.create(Contact(contactname="Adam", contactsurname="Nowak", contactnickname="Nowy", title="manager", company="INext", address=u"Kościuszki St, Wrocław", homephone="48333444555", mobilephone="48888777666", email="nowak@go.pl", byear="1977"))
    app_contact.contact.return_to_contacts_page()
    app_contact.session_contact.logout()



