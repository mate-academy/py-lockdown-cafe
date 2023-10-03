import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("Not Vaccinated")
        today_data = datetime.date.today()
        expiration_date = visitor["vaccine"]["expiration_date"]
        if today_data > expiration_date:
            raise OutdatedVaccineError("Outdated Vaccine")
        if ("wearing_a_mask" not in visitor
                or not visitor["wearing_a_mask"]):
            raise NotWearingMaskError("Not Wearing Mask")
        return f"Welcome to {self.name}"
