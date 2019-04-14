from random import randrange
from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='John', lastname='Wayne', title='Mr', company='Tradis', address='Long Island St. 77', homephone='999888777',
                                   mobilephone='123123123', email='test@test.ru', month = 'June', byear='1997'))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Devon", lastname="Nowak", email="sprawdz@sp.pp")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)