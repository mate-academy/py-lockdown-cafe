import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError. "
                                     "No vaccination")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("OutdatedVaccineError. "
                                       "Vaccine expired")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("NotWearingMaskError. "
                                      "Wear masks")
        return f"Welcome to {self.name}"
