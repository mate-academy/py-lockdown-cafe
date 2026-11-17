app/
├── __init__.py
├── main.py
├── cafe.py
└── errors.py

class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    pass

import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(
        self,
        visitor: dict,
    ) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor['name']} is not vaccinated"
            )
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor['name']}'s vaccine is outdated"
            )
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                f"{visitor['name']} is not wearing a mask"
            )
        return f"Welcome to {self.name}"

from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(
    friends: list[dict],
    cafe: Cafe,
) -> str:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"

