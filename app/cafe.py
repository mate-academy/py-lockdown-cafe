from datetime import date

from app.errors import (OutdatedVaccineError,
                        NotWearingMaskError,
                        NotVaccinatedError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        name = visitor.get("name")

        if not visitor.get("vaccine"):
            raise NotVaccinatedError(f"{name} "
                                     f"has no vaccine information.")

        expiration_date = visitor["vaccine"].get("expiration_date")
        if (not expiration_date
                or expiration_date < date.today()):
            raise OutdatedVaccineError(f"{name}'s"
                                       f" vaccine is outdated!")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(f"{name}"
                                      f" is not wearing a mask!")

        return f"Welcome to {self.name}"
