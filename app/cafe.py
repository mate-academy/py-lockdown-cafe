import datetime
from app.errors import (
    VaccineError,
    NotWearingMaskError,
    OutdatedVaccineError,
    NotVaccinatedError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(
            self,
            visitor: dict
    ) -> str | VaccineError | NotWearingMaskError:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitor vaccine is outdated")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor is not wearing a mask")
        return f"Welcome to {self.name}"
