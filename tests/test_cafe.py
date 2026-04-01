# tests/test_cafe.py
import pytest
import datetime
from app.cafe import Cafe
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


def test_visitor_without_vaccine():
    kfc = Cafe("KFC")
    visitor = {"name": "Paul", "age": 23}

    with pytest.raises(NotVaccinatedError):
        kfc.visit_cafe(visitor)


def test_visitor_with_outdated_vaccine():
    kfc = Cafe("KFC")
    visitor = {
        "name": "Paul",
        "age": 23,
        "vaccine": {"expiration_date": datetime.date(2019, 2, 23)}
    }

    with pytest.raises(OutdatedVaccineError):
        kfc.visit_cafe(visitor)


def test_visitor_without_mask():
    kfc = Cafe("KFC")
    visitor = {
        "name": "Paul",
        "age": 23,
        "vaccine": {"expiration_date": datetime.date.today()},
        "wearing_a_mask": False
    }

    with pytest.raises(NotWearingMaskError):
        kfc.visit_cafe(visitor)


def test_visitor_with_valid_vaccine_and_mask():
    kfc = Cafe("KFC")
    visitor = {
        "name": "Paul",
        "age": 23,
        "vaccine": {"expiration_date": datetime.date.today()},
        "wearing_a_mask": True
    }

    result = kfc.visit_cafe(visitor)
    assert result == "Добро пожаловать в KFC"
