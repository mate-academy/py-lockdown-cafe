import datetime
from app.errors import (NotVaccinatedError, OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today_date = datetime.date.today()

        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        elif visitor["vaccine"]["expiration_date"] < today_date:
            raise OutdatedVaccineError("The vaccine should be valid")

        elif ("wearing_a_mask" not in visitor or visitor["wearing_a_mask"]
              is False):
            raise NotWearingMaskError("Visitor should wear a mask")

        else:
            return f"Welcome to {self.name}"
