import datetime

from app.errors import (NotVaccinatedError, OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        visitor_name = visitor["name"]
        if not visitor.get("vaccine", False):
            raise NotVaccinatedError(f"{visitor_name} is not vaccinated")

        date_today = datetime.date.today()
        if visitor["vaccine"]["expiration_date"] < date_today:
            raise OutdatedVaccineError(f"{visitor_name}'s "
                                       f"vaccine has expired")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor_name} doesn't wear a mask")

        return f"Welcome to {self.name}"
