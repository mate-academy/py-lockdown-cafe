import datetime
from app.errors import (NotWearingMaskError, NotVaccinatedError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str | str, int]) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All friends should be vaccinated")

        today = datetime.date.today()

        if visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError("All friends should be vaccinated")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Friends should buy "
                                      "{masks_to_buy} masks")

        return f"Welcome to {self.name}"
