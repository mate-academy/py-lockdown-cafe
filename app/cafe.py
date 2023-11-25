import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)

day_today = datetime.date.today()


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if "vaccine" not in visitor:
            raise NotVaccinatedError()

        visitor_vaccine_date = (
            visitor.get("vaccine").get("expiration_date")
        )

        if visitor_vaccine_date < day_today:
            raise OutdatedVaccineError()

        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError()

        return f"Welcome to {self.name}"
