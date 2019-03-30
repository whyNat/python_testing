from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(contactname='John', contactsurname='Wayne', title='Mr', company='Tradis', address='Long Island St. 77', homephone='999888777',
                       mobilephone='123123123', email='test@test.ru', month = 'June', byear='1997'))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(contactname="Devon", email="sprawdz@sp.pp")
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)