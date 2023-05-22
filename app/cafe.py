import datetime


import app.errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise app.errors.NotVaccinatedError(
                f"{visitor['name']} " f"don't have vaccine!"
            )
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise app.errors.OutdatedVaccineError(
                f"{visitor['name']} have expired vaccine!"
                f" he period end on "
                f"{visitor['vaccine']['expiration_date']}"
            )
        elif visitor["wearing_a_mask"] is False:
            raise app.errors.NotWearingMaskError(f"{visitor['name']}"
                                                 f" don't have mask!")
        else:
            return f"Welcome to {self.name}"
