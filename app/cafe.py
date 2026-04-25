from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError
                        )

import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Відвідувач не вакцинований!")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Протермінована дата вакцинації!")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Вхід без маски не можливий!")
        else:
            return f"Welcome to {self.name}"
