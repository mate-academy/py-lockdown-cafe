import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        """
        Raises: NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
        wasn't added to return so as not to destroy the readability
        """
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        elif "expiration_date" in visitor["vaccine"]:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("Visitors vaccine is outdated")

        if "wearing_a_mask" not in visitor or not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
