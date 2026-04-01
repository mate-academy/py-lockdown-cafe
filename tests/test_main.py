# tests/test_main.py
import pytest
import datetime
from app.main import go_to_cafe
from app.cafe import Cafe
from app.errors import NotVaccinatedError, NotWearingMaskError


def test_go_to_cafe_all_can_go():
    friends = [
        {
            "name": "Alisa",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True
        },
    ]

    result = go_to_cafe(friends, Cafe("KFC"))
    assert result == "Друзья могут посетить KFC"


def test_go_to_cafe_all_vaccinated_but_no_mask():
    friends = [
        {
            "name": "Alisa",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": False
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": False
        },
    ]

    result = go_to_cafe(friends, Cafe("KFC"))
    assert result == "Друзья должны купить 2 масок"


def test_go_to_cafe_some_not_vaccinated():
    friends = [
        {
            "name": "Alisa",
            "wearing_a_mask": True
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True
        },
    ]

    result = go_to_cafe(friends, Cafe("KFC"))
    assert result == "Все друзья должны быть вакцинированы"
