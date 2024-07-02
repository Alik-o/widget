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
