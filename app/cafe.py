import datetime

import app.errors as err


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise err.NotVaccinatedError(
                f"Visitor {visitor['name']} has no vaccine"
            )

        if (
            visitor["vaccine"]["expiration_date"]
            < datetime.date.today()
        ):
            raise err.OutdatedVaccineError(
                f"Visitor {visitor['name']} has an outdated vaccine"
            )

        if not visitor["wearing_a_mask"]:
            raise err.NotWearingMaskError(
                f"Visitor {visitor['name']} has no mask"
            )

        return f"Welcome to {self.name}"
