import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")

        if vaccine is None:
            raise NotVaccinatedError("Should be vaccinated")

        vaccine_date = vaccine.get("expiration_date")

        if vaccine_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Should be wearing a mask")

        return f"Welcome to {self.name}"
