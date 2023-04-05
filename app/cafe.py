import datetime
import app.errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine", 0):
            if visitor["vaccine"]["expiration_date"] >= datetime.date.today():
                if not visitor["wearing_a_mask"]:
                    raise app.errors.NotWearingMaskError(
                        "The visitor should have a mask!"
                    )
            else:
                raise app.errors.OutdatedVaccineError(
                    "The visitor should get a new dose of vaccine!"
                )
        else:
            raise app.errors.NotVaccinatedError(
                "The visitor should get vaccinated!"
            )
        return f"Welcome to {self.name}"
