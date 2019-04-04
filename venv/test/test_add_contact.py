import pytest
from model.contact import Contact
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", nickname="", title="", company="", address=u"", homephone="", mobilephone="", email="", byear="")] + \
           [Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), nickname=random_string("nickname", 10), title=random_string("title", 10), company=random_string("company", 10), address=random_string("address", 30), homephone=random_string("homephone", 10), mobilephone=random_string("mobilephone", 10), workphone=random_string("workphone", 10), secondaryphone=random_string("secondaryphone", 10), email=random_string("email", 10), byear=random_string("byear", 10))
    for i in range(3)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
