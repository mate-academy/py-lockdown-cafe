from datetime import date

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError(f"{visitor.get("name")} is not vaccine")

        expiration_date = (
            visitor["vaccine"].get("expiration_date"))

        if expiration_date < date.today():
            raise (
                OutdatedVaccineError(
                    f"{visitor.get("name")}'s vaccine is outdated"))

        if not visitor.get("wearing_a_mask"):
            raise (
                NotWearingMaskError(
                    f"{visitor.get("name")} is not wear a mask"))

        return f"Welcome to {self.name}"
