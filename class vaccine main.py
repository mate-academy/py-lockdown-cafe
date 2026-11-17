class VaccineError(Exception):
    """Base exception for vaccine-related issues."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when a visitor has no vaccine record."""
    pass


class OutdatedVaccineError(VaccineError):
    """Raised when a visitor's vaccine is expired."""
    pass


class NotWearingMaskError(Exception):
    """Raised when a visitor is not wearing a mask."""
    pass

    import datetime
from errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor.get('name', 'Visitor')} is not vaccinated."
            )

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor.get('name', 'Visitor')}'s vaccine is expired."
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{visitor.get('name', 'Visitor')} is not wearing a mask."
            )

        return f"Welcome to {self.name}"

from cafe import Cafe
from errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"


    