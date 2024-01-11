from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError
from datetime import date


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "There is an absence of information about vaccination!")
        if ("vaccine" in visitor
                and visitor["vaccine"]["expiration_date"] < date.today()):
            raise OutdatedVaccineError("The vaccine is expired")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor is not wearing the mask!")
        return f"Welcome to {self.name}"
