import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def visit_cafe(self, visitor: dict) -> str:
        check = 0
        for vaccine in visitor:
            if vaccine == "vaccine":
                check += 1
        if check == 0:
            raise NotVaccinatedError(
                "All friends should be vaccinated"
            )
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "The vaccine has expired"
            )
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(
                "All visitor must have ande wear a mask!"
            )
        return f"Welcome to {self.name}"
