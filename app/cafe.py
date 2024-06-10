import datetime
from typing import Dict
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        """
        Initialize the Cafe with a name.

        Args:
            name (str): The name of the cafe.
        """
        self.name = name

    def visit_cafe(self, visitor: Dict) -> str:
        """
        Check if a visitor can enter the cafe based on vaccination and
        mask-wearing status.

        Args:
            visitor (Dict): A dictionary containing information about the
                            visitor.

        Raises:
            NotVaccinatedError: If the visitor is not vaccinated.
            OutdatedVaccineError: If the visitor's vaccine is expired.
            NotWearingMaskError: If the visitor is not wearing a mask.

        Returns:
            str: A welcome message if the visitor meets all the requirements.
        """
        vaccine_key = "vaccine"
        expiration_date_key = "expiration_date"
        mask_key = "wearing_a_mask"

        if vaccine_key not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")
        elif visitor[vaccine_key][expiration_date_key] < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is expired.")
        elif not visitor.get(mask_key, False):
            raise NotWearingMaskError("Visitor is not wearing a mask.")
        return f"Welcome to {self.name}"
