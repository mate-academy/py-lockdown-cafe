import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitors: dict) -> str:
        if not visitors.get("vaccine"):
            raise NotVaccinatedError(
                "NotVaccinatedError: Client without vaccine"
            )
        if visitors["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "OutdatedVaccineError: The client's vaccine was expired"
            )
        if not visitors.get("wearing_a_mask"):
            raise NotWearingMaskError(
                "NotWearingMaskError: Client don`t has/wear the mask"
            )
        return f"Welcome to {self.name}"
