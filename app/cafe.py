import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        # if "vaccine" not in visitor or not visitor["vaccine"]:
        if visitor.get("vaccine", 0) == 0:
            raise NotVaccinatedError("NotVaccinatedError")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("OutdatedVaccineError")
        if visitor["wearing_a_mask"] is not True:
            raise NotWearingMaskError("NotWearingMaskError")

        return f"Welcome to {self.name}"
