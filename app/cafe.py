import app.errors as error
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            if "vaccine" not in visitor:
                raise error.NotVaccinatedError("Visitor is not vaccinated.")
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise error.OutdatedVaccineError("Vaccine has expired.")
            if not visitor["wearing_a_mask"]:
                raise error.NotWearingMaskError("Visitor is not wearing mask.")
        except error.VaccineError:
            raise
        except error.NotWearingMaskError:
            raise
        return f"Welcome to {self.name}"
