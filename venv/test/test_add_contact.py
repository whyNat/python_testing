from model.contact import Contact


def test_add_contact(app):
    app.open_home_page()
    app.contact.create(Contact(contactname="Adam", contactsurname="Nowak", contactnickname="Nowy", title="manager", company="INext", address=u"Kościuszki St, Wrocław", homephone="48333444555", mobilephone="48888777666", email="nowak@go.pl", byear="1977"))
    app.contact.return_to_contacts_page()