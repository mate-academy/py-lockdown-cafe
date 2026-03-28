import datetime
from app.errors import NotWearingMaskError
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Не вацинирован")
        if visitor.get("vaccine", {}).get("expiration_date") and visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("Вакцина просрочена")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Нету маски")
        return f"Welcome to {self.name}"
