import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"Visitor {visitor['name']} " f"should be vaccinated"
            )

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                f"Vaccine already expired "
                f"at {visitor['vaccine']['expiration_date']}"
            )

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(
                f"Visitor {visitor['name']} " f"should wear a mask"
            )

        return f"Welcome to {self.name}"
