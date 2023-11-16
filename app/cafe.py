import app.errors
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if "vaccine" not in visitor:
            raise app.errors.NotVaccinatedError("Visitor is not vaccinated")

        if visitor["vaccine"]["expiration_date"] <= datetime.date.today():
            print(visitor["vaccine"]["expiration_date"])
            print(datetime.date.today())
            print("!!!!!!!!")
            raise app.errors.OutdatedVaccineError("Vaccine is outdated")

        if not visitor["wearing_a_mask"]:
            raise app.errors.NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
