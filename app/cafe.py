from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Вакцинація не знайдена.")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Вакцина протермінована.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Маска обов'язкова!")
        return f"Welcome to {self.name}"
