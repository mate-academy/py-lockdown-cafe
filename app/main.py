import datetime
from app.cafe import Cafe
from typing import Any
from app.errors import NotVaccinatedError, NotWearingMaskError, OutdatedVaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> Any:
    for friend in friends:
        try:
            Cafe.visit_cafe(cafe, friend)
        except NotVaccinatedError as a:
            return a
        except OutdatedVaccineError as b:
            return b
        except NotWearingMaskError as c:
            return c
    return "Friends can go to KFC"



friends = [
    {
        "name": "Alisa",
        "wearing_a_mask": True
    },
    {
        "name": "Bob",
        "vaccine": {
            "expiration_date": datetime.date.today()
        },
        "wearing_a_mask": True
    },
]
