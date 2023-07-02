import app.errors as er
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor:
            raise er.NotVaccinatedError
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise er.OutdatedVaccineError

        if not visitor["wearing_a_mask"]:
            raise er.NotWearingMaskError

        return f"Welcome to {self.name}"
