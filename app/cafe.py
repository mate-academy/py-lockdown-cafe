from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError
                        )
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, person: dict) -> str:
        if "vaccine" not in person.keys():
            raise NotVaccinatedError("All friends should be vaccinated")
        if person.get("vaccine").get("expiration_date")\
                < datetime.date.today():
            raise OutdatedVaccineError("All friends should be vaccinated")
        if "wearing_a_mask" not in person.keys() \
                or person.get("wearing_a_mask") is False:
            raise NotWearingMaskError("Friend should wear the mask")
        else:
            return f"Welcome to {self.name}"
