from app.errors import (NotWearingMaskError,
                        OutdatedVaccineError,
                        NotVaccinatedError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All customer have to be vaccinated!")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccines cannot be outdated!")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitors should be wearing masks!")
        else:
            return f"Welcome to {self.name}"
