from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)

import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"Dear {visitor["name"]}, please make"
                                     f"vaccine if you want to go inside cafe")

        if visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError(f"Dear {visitor["name"]}, please make"
                                       f"update of your vaccine if you"
                                       f"want to go inside")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(f"Dear {visitor["name"]}, please wear"
                                      f"a mask if you want to go inside")
        return f"Welcome to {self.name}"
