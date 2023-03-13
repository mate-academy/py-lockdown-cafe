import datetime
from app.errors import NotVaccinatedError,\
    OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        errors = 0
        masks_to_buy = 1
        if "vaccine" not in visitor:
            errors += 1
            raise NotVaccinatedError("All friends should be vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            errors += 1
            raise OutdatedVaccineError("OutdatedVaccine")
        if visitor["wearing_a_mask"] is False:
            errors += 1
            raise NotWearingMaskError(
                f"Friends should buy {masks_to_buy} masks"
            )

        return f"Welcome to {self.name}"
