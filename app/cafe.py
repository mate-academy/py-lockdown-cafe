from .errors import NotVaccinatedError
from .errors import OutdatedVaccineError
from .errors import NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(visitor.get("name", "Visitor"))

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(visitor.get("name", "Visitor"),
                                       visitor["vaccine"]["expiration_date"])

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(visitor.get("name", "Visitor"))

        else:
            return f"Welcome to {self.name}"
