from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)
import datetime


class Cafe:

    def __init__(self, name: str,) -> None:
        self.name = name

    def visit_cafe(
        self,
        visitors: dict,
    ) -> str:
        if visitors.get("vaccine") is None:
            raise NotVaccinatedError(
                "Visitors should "
                "vaccinate before visit cafe")
        elif (
            visitors["vaccine"].get("expiration_date") < datetime.date.today()
        ):
            raise OutdatedVaccineError(
                "Visitors should renew "
                "vaccine before visit cafe")
        elif visitors.get("wearing_a_mask") is False or None:
            raise NotWearingMaskError(
                "Visitor is not wearing a mask")
        else:
            return f"Welcome to {self.name}"
