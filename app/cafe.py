import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError")
        else:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("OutDatedVaccineError")
            else:
                if "wearing_a_mask" not in visitor:
                    raise NotWearingMaskError("NotWearingMaskError")
                elif not visitor["wearing_a_mask"]:
                    raise NotWearingMaskError("NotWearingMaskError")
                else:
                    return f"Welcome to {self.name}"
