import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(
            self,
            visitor: dict
    ) -> (
            NotVaccinatedError
            | OutdatedVaccineError
            | NotWearingMaskError
            | str
    ):
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("Visitor does not have a vaccine.")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is expired")
        elif visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("""To enter the cafe
            visitor must wear a mask""")
        else:
            return f"Welcome to {self.name}"
