from datetime import date
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | Exception:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("There is no vaccine")
        if visitor.get("vaccine").get("expiration_date") < date.today():
            raise OutdatedVaccineError("Expired vaccine date")
        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("Not wearing a mask")
        return f"Welcome to {self.name}"
