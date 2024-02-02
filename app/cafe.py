from datetime import date

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | Exception:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} "
                                     f"should be vaccinated.")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(f"{visitor['name']} "
                                       f"has outdated vaccine.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor['name']} should wear a mask.")
        return f"Welcome to {self.name}"
