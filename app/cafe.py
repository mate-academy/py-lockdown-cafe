from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(
            self,
            visitor: dict[str, str | int | bool | dict[str, date]]
    ) -> str | NotVaccinatedError | OutdatedVaccineError | NotWearingMaskError:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError(
                f"{visitor.get('name')} is not vaccinated"
            )
        if date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError(
                f"{visitor.get('name')} vaccination is outdated"
            )
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                f"{visitor.get('name')} is not wearing a mask"
            )
        return f"Welcome to {self.name}"
