import datetime
from app import errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        current_time = datetime.date.today()

        if "vaccine" not in visitor:
            raise errors.NotVaccinatedError("You should have vaccine")

        date_for_check = visitor["vaccine"]["expiration_date"]
        if date_for_check < current_time:
            raise errors.OutdatedVaccineError("Your vaccine is outdated")

        if visitor.get("wearing_a_mask") is False:
            raise errors.NotWearingMaskError("You should wear a mask")

        return f"Welcome to {self.name}"
