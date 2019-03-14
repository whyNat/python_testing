import pytest
from fixture.application import Application


fixture = None


@pytest.fixture                     # żeby przeglądarka otwierała się raz na całą sesję można dodać (scope='session')
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope='session', autouse=True)    # dzieje się tylko jeden raz na samym końcu, autouse - fixture zadziała automatycznie
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)


