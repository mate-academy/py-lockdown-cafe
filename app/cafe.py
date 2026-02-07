import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Need make vaccine")
        if (visitor["vaccine"]["expiration_date"]
                < datetime.date.today()):
            raise OutdatedVaccineError("Vaccine is expired")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor is not wearing a mask.")
        else:
            return f"Welcome to {self.name}"

        # try:
        #     try:
        #         if "vaccine" not in visitor:
        #             raise NotVaccinatedError("Need make vaccine")
        #         if (visitor["vaccine"]["expiration_date"]
        #                 < datetime.date.today()):
        #             raise OutdatedVaccineError("Vaccine is expired")
        #     except VaccineError:
        #         raise
        #     if not visitor["wearing_a_mask"]:
        #         raise NotWearingMaskError("Visitor is not wearing a mask.")
        # except NotWearingMaskError:
        #     raise NotWearingMaskError("Visitor is not wearing a mask.")
        # else:
        #     return f"Welcome to {self.name}"
