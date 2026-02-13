import datetime

from app.errors import (NotVaccinatedError,
                        NotWearingMaskError, OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor.get('name', 'Unknown')} "
                                     f"is Not Vaccinated")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor.get('name', 'Unknown')} "
                                       f"has Outdated Vaccine")

        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError(f"{visitor.get('name', 'Unknown')} "
                                      f"are not wearing a mask")

        return f"Welcome to {self.name}"
