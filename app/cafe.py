import datetime

from app.errors import NotVaccinatedError, NotWearingMaskError, OutdatedVaccineError

class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str :
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor has no vaccine record")
        if (visitor["vaccine"]["expiration_date"]
                and visitor["vaccine"]["expiration_date"] < datetime.date.today()):
            raise OutdatedVaccineError(f"Vaccine expired on {visitor['vaccine']['expiration_date']}")
        if visitor["wearing_a_mask"] is False :
            raise NotWearingMaskError("Visitor is not wearing a mask")
        return f"Welcome to {self.name}"
