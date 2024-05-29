import datetime
from app.errors import (
    VaccineError,
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(
            self,
            visitor: dict
    ) -> str | VaccineError | NotWearingMaskError:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("There must be a vaccine")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The vaccine must not be expired")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("There must be a mask")
        return f"Welcome to {self.name}"
