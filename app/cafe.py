from app.errors import OutdatedVaccineError, NotVaccinatedError
from app.errors import NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        if vaccine is None:
            raise NotVaccinatedError("All friends should be vaccinated")

        expiration_date = vaccine.get("expiration_date")
        if expiration_date is not None \
                and expiration_date < datetime.date.today():
            raise OutdatedVaccineError("All friends should be vaccinated")

        wearing_a_mask = visitor.get("wearing_a_mask")
        if wearing_a_mask is False:
            raise NotWearingMaskError("Friends should buy masks")

        return f"Welcome to {self.name}"
