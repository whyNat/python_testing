from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, id=None, nickname=None, title=None, company=None, address=None, homephone=None,
                 mobilephone=None, workphone=None, secondaryphone=None, email=None, email2=None, email3=None, month = None, byear=None, all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.month = month
        self.byear = byear
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return '%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s%s%s' % (self.firstname, self.lastname, self.nickname, self.title, self.company, self.address, self.homephone, self.mobilephone, self.workphone, self.secondaryphone, self.email, self.email2, self.email3, self.month, self.byear, self.id, self.all_phones_from_home_page, self.all_emails_from_home_page)   # representation - porównuje wg fizycznego rozmieszczenia obiektów w pamięci

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.lastname == other.lastname and self.firstname == other.firstname and self.nickname == other.nickname \
               and self.title == other.title and self.company == other.company and self.address == other.address and self.homephone == other.homephone and self.mobilephone == other.mobilephone and self.workphone == other.workphone and self.secondaryphone == other.secondaryphone \
               and self.email == other.email and self.email2 == other.email2 and self.email3 == other.email3 and self.month == other.month and self.byear == other.byear and self.all_phones_from_home_page == other.all_phones_from_home_page and self.all_emails_from_home_page == other.all_emails_from_home_page   # porównuje po nazwie i id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


