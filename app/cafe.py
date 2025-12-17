import datetime

from app.errors import (
    NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if ("vaccine" not in visitor
                or "expiration_date" not in visitor["vaccine"]):
            raise NotVaccinatedError("Visitor is not vaccinated!")

        vac_expire = visitor["vaccine"]["expiration_date"]
        today = datetime.date.today()
        if today > vac_expire:
            raise OutdatedVaccineError("Visitor has outdated vaccine!")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor is not wearing a mask!")

        return f"Welcome to {self.name}"
