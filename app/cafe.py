import datetime


from app.errors import (OutdatedVaccineError,
                        NotWearingMaskError,
                        NotVaccinatedError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor not vaccinated")

        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(visitor["vaccine"]["expiration_date"])

        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Wear a mask, please")

        return f"Welcome to {self.name}"
