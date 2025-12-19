import datetime
import pytest

from app import main
from app.cafe import Cafe
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


def test_visit_cafe_success():
    cafe = Cafe("KFC")
    visitor = {
        "name": "Paul",
        "age": 23,
        "vaccine": {"expiration_date": datetime.date.today()},
        "wearing_a_mask": True,
    }
    assert cafe.visit_cafe(visitor) == "Welcome to KFC"


def test_visit_cafe_no_vaccine():
    cafe = Cafe("KFC")
    visitor = {"name": "Paul", "age": 23}
    with pytest.raises(NotVaccinatedError):
        cafe.visit_cafe(visitor)


def test_visit_cafe_outdated_vaccine():
    cafe = Cafe("KFC")
    visitor = {
        "name": "Paul",
        "age": 23,
        "vaccine": {"expiration_date": datetime.date(2019, 2, 23)},
        "wearing_a_mask": True,
    }
    with pytest.raises(OutdatedVaccineError):
        cafe.visit_cafe(visitor)


def test_visit_cafe_no_mask():
    cafe = Cafe("KFC")
    visitor = {
        "name": "Paul",
        "age": 23,
        "vaccine": {"expiration_date": datetime.date.today()},
        "wearing_a_mask": False,
    }
    with pytest.raises(NotWearingMaskError):
        cafe.visit_cafe(visitor)


def test_go_to_cafe_all_good():
    cafe = Cafe("KFC")
    friends = [
        {"name": "Alisa", "vaccine": {"expiration_date": datetime.date.today()}, "wearing_a_mask": True},
        {"name": "Bob", "vaccine": {"expiration_date": datetime.date.today()}, "wearing_a_mask": True},
    ]
    assert main.go_to_cafe(friends, cafe) == "Friends can go to KFC"


def test_go_to_cafe_some_no_mask():
    cafe = Cafe("KFC")
    friends = [
        {"name": "Alisa", "vaccine": {"expiration_date": datetime.date.today()}, "wearing_a_mask": False},
        {"name": "Bob", "vaccine": {"expiration_date": datetime.date.today()}, "wearing_a_mask": False},
    ]
    assert main.go_to_cafe(friends, cafe) == "Friends should buy 2 masks"


def test_go_to_cafe_some_no_vaccine():
    cafe = Cafe("KFC")
    friends = [
        {"name": "Alisa", "wearing_a_mask": True},
        {"name": "Bob", "vaccine": {"expiration_date": datetime.date.today()}, "wearing_a_mask": True},
    ]
    assert main.go_to_cafe(friends, cafe) == "All friends should be vaccinated"
