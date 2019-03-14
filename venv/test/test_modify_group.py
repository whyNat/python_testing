from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Jonasz', header='Modify Jonasz', footer='Done'))
    app.group.modify_first_group(Group(name="new name"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Test Jonasz'))
    app.group.modify_first_group(Group(header="new header"))



