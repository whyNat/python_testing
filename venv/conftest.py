import pytest
from fixture.application import Application


fixture = None


@pytest.fixture                     # żeby przeglądarka otwierała się raz na całą sesję można dodać (scope='session')
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url)
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope='session', autouse=True)    # dzieje się tylko jeden raz na samym końcu, autouse - fixture zadziała automatycznie
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)

# wybor przegladarki z linii komend:
def pytest_addoption(parser):                   # dodaje dodatkowe parametry przy uruchomieniu z wiersza polece
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook")

