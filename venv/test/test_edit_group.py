from model.contact import ContactEdition
from model.group import GroupEdition


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(GroupEdition(name2='Janusz', footer2='longer footer'))
    app.session.logout()

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(ContactEdition(name2="Roman", email2="tetra@vn.po", month="March"))
    app.session.logout()