import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe():
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        current_date = datetime.date.today()
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError(f"{visitor["name"]} should be vaccinated")
        expiration_date = visitor.get("vaccine").get("expiration_date")
        if expiration_date < current_date:
            raise OutdatedVaccineError(f"{visitor["name"]}"
                                       f" should be vaccinated again")
        elif "wearing_a_mask" in visitor and not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor["name"]} should wear mask")

        return f"Welcome to {self.name}"
