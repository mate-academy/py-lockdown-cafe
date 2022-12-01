import datetime
import app.errors as error


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            visitor["vaccine"]
        except KeyError:
            raise error.NotVaccinatedError(
                f"Visitor {visitor['name']} is not vaccinated"
            )

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise error.OutdatedVaccineError(
                f"Visitor {visitor['name']} have expired vaccine"
            )

        if visitor["wearing_a_mask"] is False:
            raise error.NotWearingMaskError(
                f"Visitor {visitor['name']} do not wear mask"
            )

        return f"Welcome to {self.name}"
