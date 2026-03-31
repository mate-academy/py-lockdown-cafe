import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if not (vaccine := visitor.get("vaccine")):
            raise NotVaccinatedError("You haven't a vaccine passport!")
        if datetime.date.today() > vaccine.get("expiration_date"):
            raise OutdatedVaccineError(
                "Your vaccine passport period was expired!"
            )
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("You didn't wear a mask!")
        return f"Welcome to {self.name}"
