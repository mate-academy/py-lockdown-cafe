from datetime import date
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Exception | str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} has no vaccine")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(
                f"{visitor['name']} has an outdated vaccine")
        if "wearing_a_mask" not in visitor or not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor['name']} not wearing a mask")
        return f"Welcome to {self.name}"
