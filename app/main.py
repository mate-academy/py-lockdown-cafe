from datetime import date

from app.errors import NotVaccinatedError, OutdatedVaccineError, \
    NotWearingMaskError


def visit_cafe(visitor: dict) -> None:
    if not visitor["vaccine"]:
        raise NotVaccinatedError("Visitor is not vaccinated at all")

    if visitor["vaccine"]["expiration_date"] < date.today():
        raise OutdatedVaccineError("Vaccine is expired")

    if not visitor["wearing_a_mask"]:
        raise NotWearingMaskError("")


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name
