from datetime import date
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError, OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor} should "
                                     f"vaccinate before visit cafe")
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(f"{visitor} should renew "
                                       f"vaccine before visit cafe")
        elif "wearing_a_mask" not in visitor:
            raise NotWearingMaskError("please get mask")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("please get mask")
        else:
            return f"Welcome to {self.name}"
