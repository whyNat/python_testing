# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="bodyguard", header="logo", footer="takietam"))
    app.session.logout()

def test_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

def test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(contactname="Adam", contactsurname="Nowak", contactnickname="Nowy", title="manager", company="INext", address=u"Kościuszki St, Wrocław", homephone="48333444555", mobilephone="48888777666", email="nowak@go.pl", byear="1977"))
    app.contact.return_to_contacts_page()
    app.session.logout()
