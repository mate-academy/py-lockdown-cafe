import datetime
from app.errors import NotVaccinatedError
from app.errors import NotWearingMaskError
from app.errors import OutdatedVaccineError


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:

        vaccine = visitor.get("vaccine")
        if vaccine is None:
            raise NotVaccinatedError("Sorry, you have to be vacinated.")

        expiration_date = vaccine.get("expiration_date")
        today = datetime.date.today()
        if today > expiration_date:
            raise OutdatedVaccineError("Sorry, vaccinate again, please")

        has_mask = visitor.get("wearing_a_mask")
        if has_mask is None or has_mask is False:
            raise NotWearingMaskError("Please wear a mask")

        return f"Welcome to {self.name}"
