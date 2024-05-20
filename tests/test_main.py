import datetime
import inspect

import pytest

from app import main
from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    VaccineError,
    OutdatedVaccineError,
    NotWearingMaskError,
)
from app.main import go_to_cafe


def test_errors_hierarchy():
    assert NotVaccinatedError.__bases__ == (
        VaccineError,
    ), "NotVaccinatedError should inherit only VaccineError class"
    assert OutdatedVaccineError.__bases__ == (
        VaccineError,
    ), "OutdatedVaccineError should inherit only VaccineError class"
    assert (
        VaccineError not in NotWearingMaskError.__bases__
    ), "NotWearingMaskError shouldn't inherit VaccineError class"


@pytest.mark.parametrize(
    "visitor",
    [
        {
            "name": "John",
            "age": 21,
            "wearing_a_mask": True,
        },
        {
            "name": "Alisa",
            "age": 19,
            "wearing_a_mask": True,
        },
    ],
)
def test_cafe_visit_should_raise_not_vaccinated_error_when_person_does_not_have_vaccine_key(
    visitor,
):
    cafe = Cafe("")
    with pytest.raises(NotVaccinatedError) as error:
        cafe.visit_cafe(visitor)
    assert str(error.value), "NotVaccinatedError should be raised with a message"


@pytest.mark.parametrize(
    "visitor",
    [
        {
            "name": "John",
            "age": 21,
            "vaccine": {
                "name": "Pfizer",
                "expiration_date": datetime.date.today() - datetime.timedelta(days=2),
            },
            "wearing_a_mask": True,
        },
        {
            "name": "Alisa",
            "age": 19,
            "vaccine": {
                "name": "Moderna",
                "expiration_date": datetime.date.today() - datetime.timedelta(days=4),
            },
            "wearing_a_mask": True,
        },
    ],
)
def test_cafe_visit_should_raise_outdated_vaccine_error_when_vaccine_has_expired(
    visitor,
):
    cafe = Cafe("")
    with pytest.raises(OutdatedVaccineError) as error:
        cafe.visit_cafe(visitor)
    assert str(error.value), "OutdatedVaccineError should be raised with a message"


@pytest.mark.parametrize(
    "visitor",
    [
        {
            "name": "John",
            "age": 21,
            "vaccine": {
                "name": "Pfizer",
                "expiration_date": datetime.date.today() + datetime.timedelta(days=2),
            },
            "wearing_a_mask": False,
        },
        {
            "name": "Alisa",
            "age": 19,
            "vaccine": {
                "name": "Moderna",
                "expiration_date": datetime.date.today() + datetime.timedelta(days=4),
            },
            "wearing_a_mask": False,
        },
    ],
)
def test_cafe_visit_should_raise_not_wearing_mask_error_when_wearing_a_mask_is_false(
    visitor,
):
    cafe = Cafe("")
    with pytest.raises(NotWearingMaskError) as error:
        cafe.visit_cafe(visitor)
    assert str(error.value), "NotWearingMaskError should be raised with a message"


@pytest.mark.parametrize(
    "visitor,cafe_name,expected_message",
    [
        (
            {
                "name": "John",
                "age": 21,
                "vaccine": {
                    "name": "Pfizer",
                    "expiration_date": datetime.date.today(),
                },
                "wearing_a_mask": True,
            },
            "KFC",
            "Welcome to KFC",
        ),
        (
            {
                "name": "Alisa",
                "age": 19,
                "vaccine": {
                    "name": "Moderna",
                    "expiration_date": datetime.date.today()
                    + datetime.timedelta(days=4),
                },
                "wearing_a_mask": True,
            },
            "McDonald's",
            "Welcome to McDonald's",
        ),
    ],
)
def test_cafe_visit_should_return_welcome_when_visitor_is_wearing_a_mask_and_vaccinated(
    visitor, cafe_name, expected_message
):
    cafe = Cafe(cafe_name)
    assert cafe.visit_cafe(visitor) == expected_message


@pytest.mark.parametrize(
    "friends,cafe,expected_message",
    [
        (
            [
                {
                    "name": "Ivan",
                    "vaccine": {
                        "name": "Moderna",
                        "expiration_date": datetime.date.today()
                        + datetime.timedelta(days=4),
                    },
                    "wearing_a_mask": True,
                },
                {
                    "name": "Oleksii",
                    "vaccine": {
                        "name": "Pfizer",
                        "expiration_date": datetime.date.today(),
                    },
                    "wearing_a_mask": True,
                },
            ],
            Cafe("KFC"),
            "Friends can go to KFC",
        ),
        (
            [
                {
                    "name": "Alisa",
                    "vaccine": {
                        "name": "Pfizer",
                        "expiration_date": datetime.date.today()
                        + datetime.timedelta(days=30),
                    },
                    "wearing_a_mask": False,
                },
                {
                    "name": "Bob",
                    "vaccine": {
                        "name": "Pfizer",
                        "expiration_date": datetime.date.today()
                        + datetime.timedelta(days=20),
                    },
                    "wearing_a_mask": False,
                },
                {
                    "name": "Harry",
                    "vaccine": {
                        "name": "Moderna",
                        "expiration_date": datetime.date.today()
                        + datetime.timedelta(days=45),
                    },
                    "wearing_a_mask": True,
                },
            ],
            Cafe("KFC"),
            "Friends should buy 2 masks",
        ),
        (
            [
                {
                    "name": "Alisa",
                    "vaccine": {
                        "name": "Pfizer",
                        "expiration_date": datetime.date.today()
                        + datetime.timedelta(days=30),
                    },
                    "wearing_a_mask": False,
                },
                {
                    "name": "Bob",
                    "vaccine": {
                        "name": "Pfizer",
                        "expiration_date": datetime.date.today()
                        + datetime.timedelta(days=20),
                    },
                    "wearing_a_mask": False,
                },
                {
                    "name": "Harry",
                    "vaccine": {
                        "name": "Moderna",
                        "expiration_date": datetime.date.today()
                        + datetime.timedelta(days=45),
                    },
                    "wearing_a_mask": False,
                },
            ],
            Cafe("KFC"),
            "Friends should buy 3 masks",
        ),
        (
            [
                {
                    "name": "Alisa",
                    "vaccine": {
                        "name": "Pfizer",
                        "expiration_date": datetime.date.today()
                        - datetime.timedelta(days=1),
                    },
                    "wearing_a_mask": True,
                },
                {
                    "name": "Bob",
                    "vaccine": {
                        "name": "Pfizer",
                        "expiration_date": datetime.date.today()
                        + datetime.timedelta(days=20),
                    },
                    "wearing_a_mask": True,
                },
            ],
            Cafe("KFC"),
            "All friends should be vaccinated",
        ),
        (
            [
                {
                    "name": "Alisa",
                    "vaccine": {
                        "name": "Pfizer",
                        "expiration_date": datetime.date.today(),
                    },
                    "wearing_a_mask": True,
                },
                {
                    "name": "Bob",
                    "wearing_a_mask": True,
                },
            ],
            Cafe("KFC"),
            "All friends should be vaccinated",
        ),
        (
            [
                {
                    "name": "Alisa",
                    "vaccine": {
                        "name": "Pfizer",
                        "expiration_date": datetime.date.today(),
                    },
                    "wearing_a_mask": False,
                },
                {
                    "name": "Bob",
                    "wearing_a_mask": True,
                },
            ],
            Cafe("KFC"),
            "All friends should be vaccinated",
        ),
        (
            [
                {
                    "name": "Alisa",
                    "vaccine": {
                        "name": "Pfizer",
                        "expiration_date": datetime.date.today()
                        + datetime.timedelta(days=5),
                    },
                    "wearing_a_mask": False,
                },
                {
                    "name": "Bob",
                    "vaccine": {
                        "name": "Moderna",
                        "expiration_date": datetime.date.today()
                        + datetime.timedelta(days=15),
                    },
                    "wearing_a_mask": False,
                },
                {
                    "name": "Harry",
                    "vaccine": {
                        "name": "Moderna",
                        "expiration_date": datetime.date.today()
                        - datetime.timedelta(days=10),
                    },
                    "wearing_a_mask": False,
                },
            ],
            Cafe("KFC"),
            "All friends should be vaccinated",
        ),
    ],
)
def test_go_to_the_cafe(friends, cafe, expected_message):
    assert go_to_cafe(friends=friends, cafe=cafe) == expected_message


def test_comment_deleted():
    lines = inspect.getsource(main)
    assert "# write your code here" not in lines
