import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            visitor["vaccine"] == 0
        except KeyError:
            raise NotVaccinatedError("Visitor is not vaccinated")
        else:
            data_vac = visitor["vaccine"]["expiration_date"]
            if data_vac < datetime.date.today():
                raise OutdatedVaccineError("Vaccine expired")
            else:
                if visitor["wearing_a_mask"] is False:
                    raise NotWearingMaskError("NotWearingMaskError")
                else:
                    return f"Welcome to {self.name}"
