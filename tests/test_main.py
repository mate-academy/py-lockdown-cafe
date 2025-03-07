import datetime
import pytest
from app.cafe import Cafe
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
from app.main import go_to_cafe


def test_not_vaccinated():
    """Тестирует ошибку NotVaccinatedError, если у посетителя нет вакцинации."""
    cafe = Cafe("KFC")
    visitor = {"name": "Paul", "age": 23}

    with pytest.raises(NotVaccinatedError):
        cafe.visit_cafe(visitor)


def test_outdated_vaccine():
    """Тестирует ошибку OutdatedVaccineError, если вакцина просрочена."""
    cafe = Cafe("KFC")
    visitor = {
        "name": "Paul",
        "age": 23,
        "vaccine": {"expiration_date": datetime.date(2019, 2, 23)}
    }

    with pytest.raises(OutdatedVaccineError):
        cafe.visit_cafe(visitor)


def test_not_wearing_mask():
    """Тестирует ошибку NotWearingMaskError, если посетитель без маски."""
    cafe = Cafe("KFC")
    visitor = {
        "name": "Paul",
        "age": 23,
        "vaccine": {"expiration_date": datetime.date.today()},
        "wearing_a_mask": False
    }

    with pytest.raises(NotWearingMaskError):
        cafe.visit_cafe(visitor)


def test_successful_visit():
    """Тест успешного посещения кафе."""
    cafe = Cafe("KFC")
    visitor = {
        "name": "Paul",
        "age": 23,
        "vaccine": {"expiration_date": datetime.date.today()},
        "wearing_a_mask": True
    }

    assert cafe.visit_cafe(visitor) == "Welcome to KFC"


def test_friends_can_go():
    """Тест на успешный вход всех друзей в кафе."""
    friends = [
        {"name": "Alisa", "vaccine": {"expiration_date": datetime.date.today()}, "wearing_a_mask": True},
        {"name": "Bob", "vaccine": {"expiration_date": datetime.date.today()}, "wearing_a_mask": True}
    ]
    cafe = Cafe("KFC")

    assert go_to_cafe(friends, cafe) == "Friends can go to KFC"


def test_friends_need_vaccine():
    """Тест, если хотя бы один друг не вакцинирован."""
    friends = [
        {"name": "Alisa", "wearing_a_mask": True},
        {"name": "Bob", "vaccine": {"expiration_date": datetime.date.today()}, "wearing_a_mask": True}
    ]
    cafe = Cafe("KFC")

    assert go_to_cafe(friends, cafe) == "All friends should be vaccinated"


def test_friends_need_masks():
    """Тест, если некоторым друзьям нужны маски."""
    friends = [
        {"name": "Alisa", "vaccine": {"expiration_date": datetime.date.today()}, "wearing_a_mask": False},
        {"name": "Bob", "vaccine": {"expiration_date": datetime.date.today()}, "wearing_a_mask": False}
    ]
    cafe = Cafe("KFC")

    assert go_to_cafe(friends, cafe) == "Friends should buy 2 masks"
