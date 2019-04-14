import json
import os.path
import pytest
from fixture.application import Application
import importlib
import jsonpickle


fixture = None
target = None


@pytest.fixture                     # żeby przeglądarka otwierała się raz na całą sesję można dodać (scope='session')
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))  # zawiera info o lokalizacji bierzacego pliku, lokalizacja absolutna
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


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())


