import datetime

import app.errors


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        date_today = datetime.date.today()
        if "vaccine" not in visitor.keys():
            raise app.errors.NotVaccinatedError(
                "Entry is prohibited without vaccination."
            )

        elif visitor["vaccine"]["expiration_date"] < date_today:
            raise app.errors.OutdatedVaccineError(
                "Your vaccination is expired! Entry is prohibited."
            )

        elif not visitor["wearing_a_mask"]:
            raise app.errors.NotWearingMaskError("You will not pass!!!")
        else:
            return f"Welcome to {self.name}"
