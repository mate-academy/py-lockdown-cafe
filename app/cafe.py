from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
import datetime


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        date_vacine = visitor["vaccine"]["expiration_date"]
        if isinstance(date_vacine, datetime.datetime):
            date_vacine = date_vacine.date()
        date_right_now = datetime.date.today()
        if date_right_now > date_vacine:
            raise OutdatedVaccineError("The vaccine has expired")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("You need to wear a mask")
        return f"Welcome to {self.name}"
