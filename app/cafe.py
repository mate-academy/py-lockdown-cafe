from datetime import date

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            name = visitor.get("name")
            raise NotVaccinatedError(f"{name} is not vaccine")

        expiration_date = (
            visitor["vaccine"].get("expiration_date"))

        if expiration_date < date.today():
            name = visitor.get("name")
            raise (
                OutdatedVaccineError(
                    f"{name}'s vaccine is outdated"))

        if not visitor.get("wearing_a_mask"):
            name = visitor.get("name")
            raise (
                NotWearingMaskError(
                    f"{name} is not wear a mask"))

        return f"Welcome to {self.name}"
