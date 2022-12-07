import datetime


from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):

        if "vaccine" not in visitor:
            raise NotVaccinatedError("Not vaccinated")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Outdated vaccination")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("someone don't have mask")

        return f"Welcome to {self.name}"
