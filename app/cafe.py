import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("Get vaccinated")
        else:
            now_data = datetime.date.today()
            if now_data > visitor.get("vaccine")["expiration_date"]:
                raise OutdatedVaccineError("You need to be vaccinated")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Wear a protective mask")
        return f"Welcome to {self.name}"
