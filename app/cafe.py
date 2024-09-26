from typing import Union
import datetime
from app.errors import (
    NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(
            self, visitor: dict
    ) -> Union[
        str, OutdatedVaccineError, NotWearingMaskError, NotVaccinatedError
    ]:
        try:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("You should to update your vaccine")
            if not visitor["wearing_a_mask"]:
                raise NotWearingMaskError("You should wear a mask")
        except KeyError:
            raise NotVaccinatedError("You should make a vaccine")
        return f"Welcome to {self.name}"
