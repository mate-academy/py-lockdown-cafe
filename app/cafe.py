import datetime


from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated!")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Your vaccine is expired! "
                                       "Go get another shot.")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("We all know that you're handsome, "
                                      "but this time you need to cover "
                                      "your face with a mask")
        return f"Welcome to {self.name}"
