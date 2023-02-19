import datetime
from app.errors import NotWearingMaskError
from app.errors import OutdatedVaccineError
from app.errors import NotVaccinatedError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Not vaccination")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("vaccination outdated")
        if (
                "wearing_a_mask" not in visitor
                or visitor["wearing_a_mask"] is False
        ):
            raise NotWearingMaskError("Not wear mask")
        return f"Welcome to {self.name}"
