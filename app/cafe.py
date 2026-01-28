import datetime

import app.errors as e


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if "vaccine" not in visitor.keys():
            raise e.NotVaccinatedError("NotVaccinatedError")
        vaccine_date = visitor["vaccine"]["expiration_date"]

        if vaccine_date < datetime.date.today():
            raise e.OutdatedVaccineError("OutdatedVaccineError")

        if not visitor["wearing_a_mask"]:
            raise e.NotWearingMaskError("NotWearingMaskError")

        return f"Welcome to {self.name}"
