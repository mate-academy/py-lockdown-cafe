from app import errors
import datetime


class Cafe():
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if "vaccine" not in visitor.keys():
            raise errors.NotVaccinatedError("Visitor has no vaccine.")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise errors.OutdatedVaccineError("Vaccine is outdated.")
        elif not visitor.get("wearing_a_mask", False):
            raise errors.NotWearingMaskError("Visitor is not wearing a mask.")
        else:
            return f"Welcome to {self.name}"
