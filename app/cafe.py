from __future__ import annotations
import datetime

from .errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "The visitor has no information about the vaccine"
            )
        if "expiration_date" not in visitor["vaccine"] or \
                visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "The visitor's vaccine has expired"
            )
        if not visitor.get("wearing_a_mask", None) is True:
            raise NotWearingMaskError(
                "The visitor does not have a mask"
            )

        return f"Welcome to {self.name}"
