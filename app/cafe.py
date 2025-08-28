import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        date_today = datetime.date.today()
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError(
                "Entry is prohibited without vaccination."
            )

        elif visitor["vaccine"]["expiration_date"] < date_today:
            raise OutdatedVaccineError(
                "Your vaccination is expired! Entry is prohibited."
            )

        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("You will not pass!!!")
        return f"Welcome to {self.name}"
