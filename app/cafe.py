import datetime

from app.errors import (NotVaccinatedError, OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"""{visitor.get("name", "no_name")} is not vaccinated!"""
            )
        if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError(
                f"""{visitor.get("name", "no_name")}'s vaccine has expired!"""
            )
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                f"""{visitor.get("name", "no_name")} does not have a mask!"""
            )
        return f"Welcome to {self.name}"
