from datetime import date
from app.errors import NotVaccinatedError
from app.errors import NotWearingMaskError
from app.errors import OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "There is no information about vaccination!")
        if visitor.get("vaccine").get("expiration_date") < date.today():
            raise OutdatedVaccineError("The vaccine is expired")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing the mask!")
        return f"Welcome to {self.name}"
