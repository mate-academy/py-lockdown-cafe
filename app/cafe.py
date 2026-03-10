import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        if not vaccine:
            raise NotVaccinatedError(
                "Alarm! One of the clients is not vaccinated!"
            )

        expiration = vaccine.get("expiration_date")
        if expiration is None or expiration < datetime.date.today():
            raise OutdatedVaccineError(
                "Dangerous! One of the clients out of the day vaccination!"
            )

        if  not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                "Attention! One of the clients is not wearing mask!"
            )

        return f"Welcome to {self.name}"
