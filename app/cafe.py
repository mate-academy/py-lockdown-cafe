from datetime import date

from app import errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise errors.NotVaccinatedError(
                f"{visitor.get('name')} is not vaccinated"
            )

        if date.today() > visitor["vaccine"]["expiration_date"]:
            raise errors.OutdatedVaccineError(
                f"Vaccine for {visitor.get('name')} has expired"
            )

        if not visitor.get("wearing_a_mask"):
            raise errors.NotWearingMaskError(
                f"{visitor.get('name')} is not wearing a mask"
            )

        return f"Welcome to {self.name}"
