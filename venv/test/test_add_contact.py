from sys import maxsize

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(contactname="Adam", contactsurname="Nowak", contactnickname="Nowy", title="manager", company="INext", address=u"Kościuszki St, Wrocław", homephone="48333444555", mobilephone="48888777666", email="nowak@go.pl", byear="1977")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
