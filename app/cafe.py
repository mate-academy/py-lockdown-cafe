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
            raise NotVaccinatedError("All of you must have a vaccine")
        expiration_date = vaccine.get("expiration_date")
        if datetime.date.today() > expiration_date:
            raise OutdatedVaccineError("Expiration date your"
                                       " vaccine was finished")
        is_wearing_mask = visitor.get("wearing_a_mask")
        if not is_wearing_mask:
            raise NotWearingMaskError("You must wear masks")
        return f"Welcome to {self.name}"
