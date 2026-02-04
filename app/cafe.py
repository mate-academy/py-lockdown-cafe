import datetime


from app.errors import (OutdatedVaccineError,
                        NotWearingMaskError,
                        NotVaccinatedError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("Visitor must be vaccinated")
        else:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("Visitor's vaccine has expired")
            else:
                if not visitor["wearing_a_mask"]:
                    raise NotWearingMaskError("Visitor must wear a mask")
                else:
                    return f"Welcome to {self.name}"
