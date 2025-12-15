from datetime import date

from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        issues_found = 0
        if "vaccine" not in visitor:
            issues_found += 1
            raise NotVaccinatedError
        else:
            if visitor["vaccine"]["expiration_date"] < date.today():
                issues_found += 1
                raise OutdatedVaccineError
        if "wearing_a_mask" in visitor:
            if visitor["wearing_a_mask"] is False:
                issues_found += 1
                raise NotWearingMaskError
        if issues_found == 0:
            return f"Welcome to {self.name}"
