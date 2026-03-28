from datetime import date, datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe():
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All friends should be vaccinated")

        if "vaccine" in visitor:
            if "expiration_date" in visitor["vaccine"]:
                today = date.today()
                today_datetime = datetime.combine(today, datetime.min.time())
                today_seconds = int(today_datetime.timestamp())

                given_date = visitor["vaccine"]["expiration_date"]
                given_datetime = (
                    datetime.combine(given_date, datetime.min.time()))
                given_seconds = int(given_datetime.timestamp())
                if today_seconds > given_seconds:
                    raise (OutdatedVaccineError
                           ("The visitor's vaccine has expired."))

        if "wearing_a_mask" in visitor:
            if visitor["wearing_a_mask"] is False:
                raise (NotWearingMaskError
                       ("The visitor is not wearing "
                        "a mask and cannot enter the cafe."))

        return f"Welcome to {self.name}"
