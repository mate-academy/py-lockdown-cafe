from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
    VaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(
            self,
            visitor: dict
    ) -> str | VaccineError | NotWearingMaskError:

        if visitor.get("vaccine") is None:
            raise NotVaccinatedError(
                f"{visitor['name']} has not been vaccinated"
            )

        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(
                f"{visitor['name']}'s vaccine has expired"
            )

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                f"{visitor['name']} must wear a mask"
            )

        return f"Welcome to {self.name}"
