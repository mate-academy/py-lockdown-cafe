from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("No vaccine found")
        expiration = visitor["vaccine"]["expiration_date"]
        if expiration < datetime.date.today():
            raise OutdatedVaccineError("Outdated vaccine")
        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("No wearing mask found")
        return f"Welcome to {self.name}"
