import datetime
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        date_today = datetime.date.today()
        visitor_name = visitor["name"]

        if not visitor.get("vaccine"):
            raise NotVaccinatedError(f"{visitor_name}, "
                                     f"you should be vaccinated.")
        if visitor["vaccine"]["expiration_date"] < date_today:
            raise OutdatedVaccineError(f"{visitor_name},"
                                       f" you need to get vaccinated again")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor_name}, please wear a mask")

        return f"Welcome to {self.name}"
