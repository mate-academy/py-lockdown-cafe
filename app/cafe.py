from datetime import date
from app import errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise errors.NotVaccinatedError(
                "Visitors must be vaccinated in order to visit cafe.")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise errors.OutdatedVaccineError(
                "Visitor's vaccine must be up to date in order to visit cafe.")
        if not visitor.get("wearing_a_mask"):
            raise errors.NotWearingMaskError(
                "Visitors must wear a mask in order to visit cafe.")
        return f"Welcome to {self.name}"

