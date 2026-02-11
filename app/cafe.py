import datetime
from datetime import date
from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = datetime.date.today()
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        expiration_date = visitor["vaccine"].get("expiration_date")
        if (expiration_date is None
                or not isinstance(expiration_date, date)
                or expiration_date < today):
            raise OutdatedVaccineError("Visitors vaccine is outdated")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor is not wearing a mask")
        return f"Welcome to {self.name}"
