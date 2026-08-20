import datetime
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError,
                        )


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError

        now = datetime.date.today()

        if now > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
