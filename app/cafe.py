from datetime import date


from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("You should be vaccinated!")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("You should vaccinate again!")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("You should wear mask!")

        return f"Welcome to {self.name}"
