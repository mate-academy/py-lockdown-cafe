from datetime import date
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(NotVaccinatedError)
        if visitor.get("vaccine").get("expiration_date") < date.today():
            raise OutdatedVaccineError(OutdatedVaccineError)
        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError(NotWearingMaskError)
        return f"Welcome to {self.name}"
