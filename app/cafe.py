from datetime import date
from typing import Union
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Union[str, Exception]:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor should be vaccinated")
        else:
            if visitor["vaccine"]["expiration_date"] < date.today():
                raise OutdatedVaccineError("Vaccine should be up-to-date")
            else:
                if visitor["wearing_a_mask"] is False:
                    raise NotWearingMaskError("Visitor should wear a mask")
        return f"Welcome to {self.name}"
