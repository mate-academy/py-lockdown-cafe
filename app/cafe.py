import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError
                        )


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        date_today = datetime.date.today()

        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor.get('name')} is not vaccinated!")

        if visitor.get("vaccine").get("expiration_date") < date_today:
            raise OutdatedVaccineError(
                f"{visitor.get('name')} vaccine is expired")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                f"{visitor.get('name')} doesnt wear a mask!"
            )

        return f"Welcome to {self.name}"
