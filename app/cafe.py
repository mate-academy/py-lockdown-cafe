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
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("you do not have vaccine")

        if (
                visitor.get("vaccine").get("expiration_date")
                < datetime.date.today()
        ):
            raise OutdatedVaccineError("time you vaccine is over")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("you do not have a mask")

        return f"Welcome to {self.name}"
