import datetime
from app.errors import NotVaccinatedError, OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor['name']} does not have a vaccine"
            )

        current_date = datetime.date.today()
        visitor_expiration_date = visitor["vaccine"]["expiration_date"]

        if visitor_expiration_date < current_date:
            raise OutdatedVaccineError(
                f"{visitor['name']} vaccine has expired."
            )

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("All friends should wear masks")

        return f"Welcome to {self.name}"
