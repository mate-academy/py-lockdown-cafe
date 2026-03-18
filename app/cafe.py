import datetime
from app import errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        now = datetime.datetime.today().date()
        if "vaccine" not in visitor:
            raise errors.NotVaccinatedError("Visitor is not vaccinated")
        exp_date = visitor["vaccine"]["expiration_date"]
        if exp_date < now:
            raise errors.OutdatedVaccineError("Vaccine is out of date")
        elif visitor["wearing_a_mask"] is False:
            raise errors.NotWearingMaskError("Visitor is not wearing a mask")
        return f"Welcome to {self.name}"
