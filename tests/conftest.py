import pytest


@pytest.fixture
def no_data():
    return ""


@pytest.fixture
def more_required_amount():
    return "25331736541084301358743051135"


@pytest.fixture
def less_required_amount():
    return "33656"


@pytest.fixture
def list_transaction_data():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594333727, "date": "2018-09-12T21:27:25.241689"},
        {"id": 615841591, "date": "2018-10-14T08:21:33.419441"},
    ]
