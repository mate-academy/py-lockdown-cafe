from datetime import date

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        exception_counter = 0

        if not visitor.get("vaccine"):
            exception_counter += 1
            raise NotVaccinatedError("For visiting our cafe, everybody "
                                     "should be vaccinated and you, "
                                     f"{visitor['name']}, "
                                     "are not an exception!")

        if visitor["vaccine"]["expiration_date"] < date.today():
            exception_counter += 1
            raise OutdatedVaccineError("Your vaccine is expired! Go away!")

        if not visitor["wearing_a_mask"]:
            exception_counter += 1
            raise NotWearingMaskError("We don't want to die because of you! "
                                      "Wear the mask!")

        if not exception_counter:
            return f"Welcome to {self.name}"
