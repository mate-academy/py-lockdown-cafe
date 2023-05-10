from app.errors import NotVaccinatedError,\
    OutdatedVaccineError, NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        wearing_mask = visitor.get("wearing_a_mask", False)

        if vaccine is None:
            raise NotVaccinatedError("All friends should be vaccinated")

        expiration_date = vaccine.get("expiration_date")
        if expiration_date is not None and \
                expiration_date < datetime.date.today():
            raise OutdatedVaccineError("All friends should be vaccinated")

        if not wearing_mask:
            raise NotWearingMaskError("All friends should wear masks")

        return f"Welcome to {self.name}"
