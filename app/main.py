import datetime


class VaccineError(Exception):
    """problems with the vaccine"""


class NotVaccinatedError(VaccineError):
    """If there is no vaccine"""


class OutdatedVaccineError(VaccineError):
    """The vaccination period is over"""


class NotWearingMaskError(Exception):
    """Visitor without a mask"""


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError
        return f"Welcome to {self.name}"


def go_to_cafe(friends: list, cafe: Cafe):
    masks_to_buy = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return f"All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
        else:
            return f"Friends can go to {cafe.name}"
    return f"Friends should buy {masks_to_buy} masks"



