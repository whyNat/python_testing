import pytest
from fixture.application import Application


@pytest.fixture(scope = 'session')   # przeglądarka otwiera się raz na całą sesję
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

