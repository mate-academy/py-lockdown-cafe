import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        print(f"Visitor data received: {visitor}")
        if "vaccine" not in visitor:
            print("Vaccine key missing. Raising NotVaccinatedError.")
            raise NotVaccinatedError("Visitor is not vaccinated.")
        today_date = datetime.date.today()
        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date < today_date:
            raise OutdatedVaccineError("Visitor's vaccine is outdated.")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                "You should wear a mask to enter the cafe!"
            )
        return f"Welcome to {self.name}"
