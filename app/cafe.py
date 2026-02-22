import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe():
    def __init__(self, name: str) -> None:
        self.name = name

    # @staticmethod
    def visit_cafe(self, visitor: dict) -> str:
        # expiration_date = visitor["vaccine"]["expiration_date"]
        current_datetime = datetime.datetime.now().date()

        if "vaccine" not in visitor:
            raise NotVaccinatedError("Friend is not vaccinated")

        expiration_date = visitor["vaccine"].get("expiration_date", None)

        if expiration_date is None:
            raise OutdatedVaccineError("Missing expiration date for vaccine")
        elif expiration_date < current_datetime:
            raise OutdatedVaccineError("Outdated Vaccine")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Someone Is Not Wearing the Mask")
        else:
            return f"Welcome to {self.name}"
