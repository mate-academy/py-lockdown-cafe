import datetime


from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | type:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("The visitor is not vaccinated")

        if (
                visitor.get("vaccine").get("expiration_date")
                < datetime.date.today()
        ):
            raise OutdatedVaccineError("The visitor's vaccine has expired")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("The visitor is not wearing a mask")

        return f"Welcome to {self.name}"
