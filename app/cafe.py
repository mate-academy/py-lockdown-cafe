import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f'Visitor {visitor.get("name", "Unknown")} is not vaccinated.'
            )

        vaccine_info = visitor["vaccine"]
        expiration_date = vaccine_info.get("expiration_date")
        if not expiration_date or not isinstance(
            expiration_date, datetime.date
        ):
            raise ValueError(
                f'Invalid expiration_date for visitor {
                    visitor.get(
                        "name", "Unknown")}.'
            )

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f'Vaccine expired for visitor {
                    visitor.get(
                        "name", "Unknown")}.'
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f'Visitor {
                    visitor.get(
                        "name",
                        "Unknown")} is not wearing a mask.'
            )

        return f'Welcome to {self.name}'
