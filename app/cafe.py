from datetime import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.today().date():
            raise OutdatedVaccineError("The vaccine is expired, entry denied.")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor "
                                      "must wear a mask to enter the cafe.")
        return f"Welcome to {self.name}"
