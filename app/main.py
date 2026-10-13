from datetime import date


class CafeError(Exception):
    pass


class NotVaccinatedError(CafeError):
    pass


class OutdatedVaccineError(CafeError):
    pass


class NotWearingMaskError(CafeError):
    pass


class Cafe:
    def __init__(self, name: str):
        self.name = name


def visit_cafe(visitor: dict, cafe: Cafe) -> str:
    vaccine = visitor.get("vaccine")
    if not vaccine:
        raise NotVaccinatedError("Visitor is not vaccinated")
    if vaccine.get("expiration_date") < date.today():
        raise OutdatedVaccineError("Vaccine is outdated")
    if not visitor.get("wearing_a_mask", False):
        raise NotWearingMaskError("Visitor is not wearing a mask")
    return f"Welcome to {cafe.name}"


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    for friend in friends:
        visit_cafe(friend, cafe)
    return f"Friends can go to {cafe.name}"
