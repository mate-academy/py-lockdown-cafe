import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, dict_: dict) -> str:
        today = datetime.date.today()

        if "vaccine" not in dict_:
            raise NotVaccinatedError("Visitor is not vaccinated")
        expiration_date = dict_["vaccine"]["expiration_date"]

        if today > expiration_date:
            raise OutdatedVaccineError("Visitor's vaccine is outdated")

        if dict_["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
