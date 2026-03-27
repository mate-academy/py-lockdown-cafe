from typing import Optional
import datetime
from app.errors import (OutdatedVaccineError,
                        NotVaccinatedError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name : str) -> None:
        self.name = name

    def visit_cafe(self, visitor : dict) -> Optional[str]:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor not vaccinated.")
        else:
            if "expiration_date" in visitor["vaccine"]:
                cond = (datetime.date.today()
                        > visitor["vaccine"]["expiration_date"])
                if cond:
                    raise OutdatedVaccineError("Vaccine expired.")

        if "wearing_a_mask" in visitor:
            if visitor["wearing_a_mask"] is False:
                raise NotWearingMaskError("Visitor has no mask.")
        else:
            raise NotWearingMaskError("Visitor has no mask.")

        return f"Welcome to {self.name}"
