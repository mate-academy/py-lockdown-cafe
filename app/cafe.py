from __future__ import annotations

import datetime

from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError()

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError()

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError()

        return f"Welcome to {self.name}"
