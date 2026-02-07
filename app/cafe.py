import datetime

from app.errors import (VaccineError, NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            try:
                if "vaccine" not in visitor:
                    raise NotVaccinatedError("Need make vaccine")
                if (visitor["vaccine"]["expiration_date"]
                        < datetime.date.today()):
                    raise OutdatedVaccineError
            except VaccineError:
                raise
            if not visitor["wearing_a_mask"]:
                raise NotWearingMaskError
        except NotWearingMaskError:
            raise NotWearingMaskError
        else:
            return f"Welcome to {self.name}"
