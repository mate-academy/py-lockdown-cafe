from datetime import date

import app.errors as errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise errors.NotVaccinatedError(
                f"{visitor.get('name')} not vaccinated!"
            )

        if visitor["vaccine"].get("expiration_date") < date.today():
            raise errors.OutdatedVaccineError(
                f"Vaccine of {visitor.get('name')} is expired!"
            )

        if not visitor.get("wearing_a_mask", False):
            raise errors.NotWearingMaskError(
                f"{visitor.get('name')} "
                "must wear a medical mask to visit!"
            )

        return f"Welcome to {self.name}"
