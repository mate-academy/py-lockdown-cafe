import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        data1 = datetime.date.today()
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor is not vaccinated")
        elif visitor.get("vaccine").get("expiration_date") < data1:
            raise OutdatedVaccineError("Visitor's vaccine expired")
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                f"{visitor.get('name')} is not wearing a mask"
            )
        return f"Welcome to {self.name}"
