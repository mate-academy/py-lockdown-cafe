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
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor must have the vaccine")
        expiration_date = visitor.get("vaccine", dict()).get("expiration_date")
        if (expiration_date is not None
                and expiration_date < datetime.date.today()):
            raise OutdatedVaccineError("The vaccine must not be expired")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor must wear a mask")
        return f"Welcome to {self.name}"
