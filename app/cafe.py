import app.errors as error
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise error.NotVaccinatedError(
                f"Visitor {visitor['name']} has no vaccine"
            )

        if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise error.OutdatedVaccineError(
                f"Visitor {visitor['name']} has an outdated vaccine"
            )

        if visitor["wearing_a_mask"] is False:
            raise error.NotWearingMaskError(
                "Visitor {visitor['name']} has no mask"
            )
        return f"Welcome to {self.name}"
