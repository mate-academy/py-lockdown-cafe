import datetime
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"Visitor {visitor.get('name', 'Unknown')} is not vaccinated"
            )

        expiry_date = visitor["vaccine"]["expiration_date"]
        if expiry_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"Visitor {visitor.get('name', 'Unknown')} has an expired vaccine "
                f"on {expiry_date:%Y-%m-%d}"
            )

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                f"Visitor {visitor.get('name', 'Unknown')} is not wearing a mask"
            )

        return f"Welcome to {self.name}"