import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    """Klasa przedstawiająca kafejkę"""

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        """Metoda sprawdzająca możlwość wejscia klienta do kafejki"""

        data_today = datetime.date.today()
        data_time_dict = visitor.get("vaccine")

        if data_time_dict is None:
            raise NotVaccinatedError("Visitor is not vaccinated")
        data_time = data_time_dict.get("expiration_date")
        if data_time is None or data_today > data_time:
            raise OutdatedVaccineError("Vaccine is outdated")
        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError(
                "Visitor is not wearing a mask"
            )
        return (f"Welcome to {self.name}")
