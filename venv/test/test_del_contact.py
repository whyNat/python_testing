from random import randrange
from time import sleep

from model.contact import Contact


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(contactname='John', contactsurname='Wayne', title='Mr', company='Tradis', address='Long Island St. 77', homephone='999888777',
                       mobilephone='123123123', email='test@test.ru', month = 'June', byear='1997'))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    sleep(4)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index + 1] = []  # usuwa wybrany losowo kontakt
    assert old_contacts == new_contacts
