import datetime
from app.errors import NotVaccinatedError, OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if (not visitor or not isinstance(visitor, dict)
                or not visitor.get("vaccine")):
            raise NotVaccinatedError("Visitor is not vaccinated")

        vaccine_date = visitor.get("vaccine").get("expiration_date")
        if (not vaccine_date or not isinstance(vaccine_date, datetime.date)
                or vaccine_date < datetime.date.today()):
            raise OutdatedVaccineError(f"The vaccine of {visitor.get('name')} "
                                       f"is expired")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"Visitor {visitor.get('name')} "
                                      f"without mask")

        return f"Welcome to {self.name}"
