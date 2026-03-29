import datetime
from typing import Dict, Any
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    """Represents a cafe with a name."""

    def __init__(self, name: str) -> None:
        """
        Initializes a Cafe object.

        Args:
            name: The name of the cafe.
        """
        self.name = name

    def visit_cafe(self, visitor: Dict[str, Any]) -> str:
        """
        Allows a visitor to enter the cafe if they meet all the requirements.

        Args:
            visitor: A dictionary containing visitor information.

        Raises:
            NotVaccinatedError: If the visitor does not have a vaccine.
            OutdatedVaccineError: If the vaccine is expired.
            NotWearingMaskError: If the visitor is not wearing a mask.

        Returns:
            str: A welcome message.
        """
        visitor_name: str = visitor.get("name", "Unknown Visitor")

        if "vaccine" not in visitor:
            raise NotVaccinatedError(visitor_name)

        expiration_date = visitor["vaccine"].get("expiration_date")
        if not isinstance(expiration_date,
                          datetime.date):
            raise ValueError("Vaccine expiration_date "
                             "must be a datetime.date object.")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(visitor_name, expiration_date)

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(visitor_name)

        return f"Welcome to {self.name}"
