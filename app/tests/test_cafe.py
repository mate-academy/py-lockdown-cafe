import datetime
import pytest

from cafe import Cafe
from errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


def test_visit_cafe_success():
    cafe = Cafe("KFC")
    visitor = {
        "name": "Paul",
        "age": 30,
        "vaccine": {"expiration_date": datetime.date.today()},
        "wearing_a_mask": True,
    }
    assert cafe.visit_cafe(visitor) == "Welcome to KFC"


def test_visit_cafe_not_vaccinated():
    cafe = Cafe("KFC")
    visitor = {
        "name": "Paul",
        "age": 30,
        "wearing_a_mask": True,
    }
    with pytest.raises(NotVaccinatedError):
        cafe.visit_cafe(visitor)


def test_visit_cafe_outdated_vaccine():
    cafe = Cafe("KFC")
    visitor = {
        "name": "Paul",
        "age": 30,
        "vaccine": {"expiration_date": datetime.date(2020, 1, 1)},
        "wearing_a_mask": True,
    }
    with pytest.raises(OutdatedVaccineError):
        cafe.visit_cafe(visitor)


def test_visit_cafe_not_wearing_mask():
    cafe = Cafe("KFC")
    visitor = {
        "name": "Paul",
        "age": 30,
        "vaccine": {"expiration_date": datetime.date.today()},
        "wearing_a_mask": False,
    }
    with pytest.raises(NotWearingMaskError):
        cafe.visit_cafe(visitor)
