import datetime
import app.errors as error


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise error.NotVaccinatedError
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise error.OutdatedVaccineError
        if visitor["wearing_a_mask"] is False:
            raise error.NotWearingMaskError
        return f"Welcome to {self.name}"
