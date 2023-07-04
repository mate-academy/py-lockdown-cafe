import datetime
from .errors import NotVaccinatedError, OutdatedVaccineError
from .errors import NotWearingMaskError


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = datetime.date.today()
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("NotVaccinatedError")
        else:
            expiration_date = visitor["vaccine"]["expiration_date"]
        if today > expiration_date:
            raise OutdatedVaccineError("OutdatedVaccineError")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("NotWearingMaskError")
        return f"Welcome to {self.name}"
