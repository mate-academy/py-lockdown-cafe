import datetime
from app import errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise errors.NotVaccinatedError(
                "Everyone should be vaccinated")
        current_date = datetime.date.today()
        if visitor["vaccine"]["expiration_date"] < current_date:
            raise errors.OutdatedVaccineError(
                "Everyone should have a valid vaccine")
        if not visitor["wearing_a_mask"]:
            raise errors.NotWearingMaskError(
                "Everyone should wear a face mask")
        return f"Welcome to {self.name}"
