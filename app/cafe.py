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
        vaccinated = visitor.get("vaccine")
        current_date = datetime.date.today()
        mask_on_face = visitor["wearing_a_mask"]
        vaccine_exp = vaccinated["expiration_date"] if vaccinated else None

        if vaccinated is None:
            raise NotVaccinatedError("Beware, conspiracy theorist")

        if vaccine_exp < current_date:
            raise OutdatedVaccineError("Person without plans")

        if not mask_on_face:
            raise NotWearingMaskError("Big nose person!")

        return f"Welcome to {self.name}"
