import datetime
import app.errors as err


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise err.NotVaccinatedError("Visitor is not vaccinated")

        visitor_vaccine = visitor["vaccine"]

        if visitor_vaccine["expiration_date"] < datetime.date.today():
            raise err.OutdatedVaccineError("Visitor vaccination is outdated")

        if not visitor["wearing_a_mask"]:
            raise err.NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
