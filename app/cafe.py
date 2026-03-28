import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor.get('name', 'Unknown')} "
                                     f"is not vaccinated.")

        expiration = visitor["vaccine"].get("expiration_date")
        if not isinstance(expiration, datetime.date):
            raise OutdatedVaccineError(
                f"{visitor['name']}'s vaccine expiration date "
                f"must be a datetime.date object, got "
                f"{type(expiration).__name__}"
            )
        if expiration < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor['name']}'s "
                                       f"vaccine is expired on {expiration}")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"{visitor['name']} "
                                      f"is not wearing a mask")

        return f"Welcome to {self.name}"
