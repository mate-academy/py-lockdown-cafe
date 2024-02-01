import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor must be vaccinated!")
        if "vaccine" in visitor:
            expiration = visitor["vaccine"]["expiration_date"]
            if expiration < datetime.date.today():
                raise OutdatedVaccineError("Vaccination must "
                                           "be is not expired!")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitors must wear masks!")
        return f"Welcome to {self.name}"

    def __str__(self) -> str:
        return self.name
