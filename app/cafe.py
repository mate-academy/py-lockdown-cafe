from app.errors import (NotVaccinatedError,
                        NotWearingMaskError, OutdatedVaccineError)
import datetime


class Cafe:
    name = ""

    def __init__(self, name: str) -> None:
        global current_cafe_name
        self.name = name
        current_cafe_name = name


def visit_cafe(visitor: dict) -> str:
    if "vaccine" not in visitor:
        raise NotVaccinatedError("Visitor is not vaccinated")
    else:
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is outdated")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor is not wearing mask")
        return f"Welcome to {current_cafe_name}"
