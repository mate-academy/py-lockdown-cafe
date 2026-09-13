from datetime import date

from app.errors import (
    VaccineError,
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            if "vaccine" in visitor.keys():
                vaccine_datetime = visitor["vaccine"]["expiration_date"]

                if date.today() > vaccine_datetime:
                    raise OutdatedVaccineError("Vaccine date is expired")

                if visitor["wearing_a_mask"] is False:
                    raise NotWearingMaskError("Visitor does not have a mask")
            else:
                raise NotVaccinatedError("Visitor is not vaccinated")
        except VaccineError as ex:
            raise ex
        else:
            return f"Welcome to {self.name}"
