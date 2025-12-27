import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        # Check if visitor is vaccinated
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor.get('name', 'Visitor')} is "
                                     f"not vaccinated.")

        # Check if vaccine is not outdated
        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor.get('name', 'Visitor')}'s "
                                       f"vaccine is outdated.")

        # Check if visitor is wearing a mask
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"{visitor.get('name', 'Visitor')} is "
                                      f"not wearing a mask.")

        # All checks passed
        return f"Welcome to {self.name}"
