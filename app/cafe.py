import datetime


from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"Visitor {visitor['name']} "
                                     f"not vaccinated")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"Visitor's {visitor['name']} "
                                       f"vaccine is expired")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(f"Visitor's {visitor['name']} "
                                      f"should wear some masks")

        return f"Welcome to {self.name}"
