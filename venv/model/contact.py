from sys import maxsize


class Contact:
    def __init__(self, contactname=None, contactsurname=None, contactnickname=None, title=None, company=None, address=None, homephone=None,
                       mobilephone=None, email=None, month = None, byear=None, id=None):
        self.contactname = contactname
        self.contactsurname = contactsurname
        self.contactnickname = contactnickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.email = email
        self.month = month
        self.byear = byear
        self.id = id

    def __repr__(self):
        return '%s:%s' % (self.id, self.contactsurname)   # representation - porównuje wg fizycznego rozmieszczenia obiektów w pamięci

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.contactsurname == other.contactsurname      # porównuje po nazwie i id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


