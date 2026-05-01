import datetime

from app.errors import (
    OutdatedVaccineError,
    NotVaccinatedError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" in visitor:
            date1 = visitor["vaccine"]["expiration_date"]
            date2 = datetime.date.today()
            if date1 >= date2:
                if visitor["wearing_a_mask"]:
                    return f"Welcome to {self.name}"
                raise NotWearingMaskError("You have to wear a chin diaper")
            raise OutdatedVaccineError(
                f"Vaccine has expired on "
                f"{visitor['vaccine']['expiration_date']}"
            )
        raise NotVaccinatedError("You are not vaccinated")
