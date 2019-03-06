
class Contact:
    def __init__(self, contactname, contactsurname, contactnickname, title, company, address, homephone,
                       mobilephone, email, byear):
        self.contactname = contactname
        self.contactsurname = contactsurname
        self.contactnickname = contactnickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.email = email
        self.byear = byear

class ContactEdition:
    def __init__(self, name2, email2, month):
        self.name2 = name2
        self.email2 = email2
        self.month = month
