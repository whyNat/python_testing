import jsonpickle
from model.contact import Contact
import random
import string
import os.path
import getopt   # do czytania opcji wiersza polecen
import sys      # dla dostepu do tych opcji


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", nickname="", title="", company="", address="", homephone="",
                 mobilephone="", workphone="", secondaryphone="", email="", email2="", email3="", month="", byear="")] + [
    Contact(firstname=random_string("firstname", 20), lastname=random_string("lastname", 20), nickname=random_string("nickname", 20), title=random_string("title", 20), company=random_string("company", 20), address=random_string("address", 20), homephone=random_string("homephone", 20), mobilephone=random_string("mobilephone", 20), workphone=random_string("workphone", 20), secondaryphone=random_string("secondaryphone", 20), email=random_string("email", 20), email2=random_string("email2", 20), email3=random_string("email3", 20), month=random_string("month", 20), byear=random_string("byear", 20))
    for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))