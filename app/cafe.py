import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Please take a vaccine!")
        else:
            timestamp = datetime.date.today()
            if "expiration_date" not in visitor["vaccine"]:
                raise OutdatedVaccineError("Missing expiration date!")
            else:
                if visitor["vaccine"]["expiration_date"] < timestamp:
                    raise OutdatedVaccineError("Outdated vaccine!")

        if "wearing_a_mask" not in visitor:
            raise NotWearingMaskError("Wearing a mask is mandatory!")
        else:
            if not visitor["wearing_a_mask"]:
                raise NotWearingMaskError("Wearing a mask is mandatory!")

        return f"Welcome to {self.name}"
