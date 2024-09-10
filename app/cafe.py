import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor.get('name', 'Visitor')} "
                                     f"does not have a vaccine.")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor.get('name', 'Visitor')}'s "
                                       f"vaccine is outdated.")
        if not visitor.get("wearing_a_mask", True):
            raise NotWearingMaskError(f"{visitor.get('name", "Visitor')} "
                                      f"is not wearing a mask.")
        return f"Welcome to {self.name}"
