import datetime
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError, OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor or not visitor["vaccine"]:
            raise NotVaccinatedError("Visitor is not vaccinated.")
        print(f"Welcome to {self.name}, {visitor.get("name", "Guest")}!")

        vaccine_info = visitor["vaccine"]
        if "expiration_date" not in vaccine_info:
            raise OutdatedVaccineError("Vaccine expiration date is missing.")
        expiration_date = vaccine_info["expiration_date"]
        if isinstance(expiration_date, str):
            expiration_date = (datetime.datetime.
                               strptime(expiration_date, "%Y-%m-%d").date())

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is expired.")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor is not wearing a mask "
                                      "and cannot enter the cafe.")

        return f"Welcome to {self.name}"
