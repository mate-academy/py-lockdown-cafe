import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"Visitor {visitor['name']}"
                                     f" is not vaccinated")

        expiration = visitor["vaccine"].get("expiration_date")
        if expiration is None:
            raise OutdatedVaccineError(f"Visitor {visitor['name']}"
                                       f" has no expiration_date")

        if expiration < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor['name']}"
                                       f" has outdated vaccine")

        if ("wearing_a_mask" not in visitor
                or visitor["wearing_a_mask"] is False):

            raise NotWearingMaskError(f"{visitor['name']}"
                                      f" should wear a mask")

        return f"Welcome to {self.name}"
