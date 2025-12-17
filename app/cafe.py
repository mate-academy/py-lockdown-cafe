import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
    VaccineMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = datetime.date.today()
        if (("vaccine" not in visitor
            or visitor["vaccine"]["expiration_date"] < today)
                and not visitor["wearing_a_mask"]):
            raise VaccineMaskError(
                "Visitor is not vaccine and s not wearing a mask")
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccine")
        if visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError("Visitor is not vaccine")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor is not wearing a mask")
        return f"Welcome to {self.name}"
