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
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f'The {visitor["name"]} don\'t have a vaccine'
            )

        expiration_date = visitor["vaccine"]["expiration_date"]
        today_day = datetime.date.today()

        if expiration_date < today_day:
            raise OutdatedVaccineError("The vaccine must not be expired")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("all visitors must wear masks")

        return f"Welcome to {self.name}"
