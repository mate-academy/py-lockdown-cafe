from .errors import NotVaccinatedError
from .errors import OutdatedVaccineError
from .errors import NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor must have a vaccine.")

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date is None or expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                "Visitor's vaccine is either missing or expired."
            )

        if not visitor.get("wearing_a_mask", True):
            raise NotWearingMaskError("Visitor must be wearing a mask.")

        return f"Welcome to {self.name}"
