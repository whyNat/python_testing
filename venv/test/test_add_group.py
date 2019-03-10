# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="bodyguard", header="logo", footer="takietam"))

def test_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

def test_add_contact(app):
    app.open_home_page()
    app.contact.create(Contact(contactname="Adam", contactsurname="Nowak", contactnickname="Nowy", title="manager", company="INext", address=u"Kościuszki St, Wrocław", homephone="48333444555", mobilephone="48888777666", email="nowak@go.pl", byear="1977"))
    app.contact.return_to_contacts_page()
