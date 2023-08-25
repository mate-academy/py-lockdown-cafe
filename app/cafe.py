import datetime
from app.errors import NotWearingMaskError
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" in visitor:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("All friends should be vaccinated")
        else:
            raise NotVaccinatedError(
                "If you want to enter to the cafe you must do vaccine!"
            )

        if visitor.get("wearing_a_mask") is not True:
            raise NotWearingMaskError(
                "If you want to enter to the cafe you must wear mask!"
            )

        return f"Welcome to {self.name}"
