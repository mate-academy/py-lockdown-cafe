import datetime
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError, OutdatedVaccineError)


class Cafe:
    def __init__(
            self,
            name: str
    ) -> None:
        self.name = name

    def visit_cafe(
            self,
            visitor: dict
    ) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date and expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor has outdated vaccine")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
