from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All friends should be vaccinated")
        if "vaccine" in visitor:
            current_time = datetime.date.today()
            expiration_date = visitor["vaccine"]["expiration_date"]
            if current_time > expiration_date:
                raise OutdatedVaccineError("All friends should be vaccinated")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("NotWearingMaskError")

        return f"Welcome to {self.name}"
