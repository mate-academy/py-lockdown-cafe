import datetime
from app import errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        now = datetime.datetime.today().date()
        if "vaccine" not in visitor:
            raise errors.NotVaccinatedError("NotVaccinatedError")
        exp_date = visitor["vaccine"]["expiration_date"]
        if exp_date < now:
            raise errors.OutdatedVaccineError("OutdatedVaccineError")
        elif visitor["wearing_a_mask"] is False:
            raise errors.NotWearingMaskError("NotWeraingMaskError")
        else:
            return f"Welcome to {self.name}"
