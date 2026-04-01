import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(f"{visitor['name']} "
                                     f"should be vaccinated.")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor['name']}\'s "
                                       f"vaccine is expired.")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(f"{visitor['name']} "
                                      f"should wear a mask.")
        return f"Welcome to {self.name}"
