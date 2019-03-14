from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(contactname='John', contactsurname='Wayne', title='Mr', company='Tradis', address='Long Island St. 77', homephone='999888777',
                       mobilephone='123123123', email='test@test.ru', month = 'June', byear='1997'))
    app.contact.delete_first_contact()