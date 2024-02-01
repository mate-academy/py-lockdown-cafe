from app.errors import (NotVaccinatedError, NotWearingMaskError,
                        OutdatedVaccineError, VaccineError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            if "vaccine" not in visitor.keys():
                raise NotVaccinatedError("Visitor don`t have vaccine")
            expiration_date = visitor["vaccine"].get("expiration_date")
            if expiration_date < datetime.date.today():
                raise OutdatedVaccineError("Vaccine is outdated")
            if not visitor.get("wearing_a_mask", False):
                raise NotWearingMaskError("Visitor is not wearing a mask")
            return f"Welcome to {self.name}"
        except VaccineError as e:
            raise e
