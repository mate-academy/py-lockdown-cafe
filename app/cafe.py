import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe():
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            if not visitor.get("vaccine"):
                raise NotVaccinatedError("You are not vaccinated.")
            elif (visitor.get("vaccine").get("expiration_date")
                  < datetime.date.today()):
                raise OutdatedVaccineError("The vaccine must not be expired!")
            elif not visitor.get("wearing_a_mask"):
                raise NotWearingMaskError("All visitors must wear masks!")
        except Exception:
            raise
        else:
            return f"Welcome to {self.name}"
