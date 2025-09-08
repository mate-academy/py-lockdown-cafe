import datetime

from app.errors import NotVaccinatedError, NotWearingMaskError, OutdatedVaccineError

class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str :
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor has no vaccine record")
        if (visitor.get("vaccine", {}).get("expiration_date") and
                visitor.get("vaccine", {}).get("expiration_date") < datetime.date.today()):
            raise OutdatedVaccineError(f"Vaccine expired on {visitor['vaccine']['expiration_date']}")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing a mask")
        return f"Welcome to {self.name}"
