from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        expiration_date = visitor["vaccine"].get("expiration_date")
        if isinstance(expiration_date, str):
            expiration_date = datetime.datetime.strptime(visitor["vaccine"]
                                                .get("expiration_date"),
                                                "%Y-%m-%d").date()
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated")
        if "wearing_a_mask" not in visitor or not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor is not wearing a mask")
        else:
            return f"Welcome to {self.name}"
