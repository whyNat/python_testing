import json
import os.path
import pytest
from fixture.application import Application


fixture = None
target = None


@pytest.fixture                     # żeby przeglądarka otwierała się raz na całą sesję można dodać (scope='session')
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption(
            "--target"))  # zawiera info o lokalizacji bierzacego pliku, lokalizacja absolutna
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or fixture.is_valid():
        fixture = Application(browser=browser, base_url=target["baseUrl"])
    fixture.session.ensure_login(username=target["username"], password=target["password"])
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
    parser.addoption("--target", action="store", default="target.json")

