import datetime

import app.errors as errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise errors.NotVaccinatedError("All friends should be vaccinated")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise errors.OutdatedVaccineError("All friends should be "
                                              "vaccinated")
        elif not visitor.get("wearing_a_mask", True):
            raise errors.NotWearingMaskError("Friends should buy masks")
        else:
            return f"Welcome to {self.name}"
