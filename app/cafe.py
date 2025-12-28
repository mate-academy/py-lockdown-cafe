import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    """Represents a cafe that enforces vaccination and mask rules.

    Attributes:
        name (str): Cafe name used in welcome messages.
    """

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        """Validate a visitor and return a welcome message if allowed.

        Rules checked (in order):
        1. Visitor must have a `vaccine` key, otherwise
            NotVaccinatedError is raised.
        2. `vaccine` must include `expiration_date`; missing date
            raises NotVaccinatedError.
        3. `expiration_date` must be >= today's date; otherwise
            OutdatedVaccineError is raised.
        4. Visitor must have `wearing_a_mask` truthy; otherwise
            NotWearingMaskError is raised.

        Args:
            visitor (dict): Visitor information. Expected keys:
                - "name" (optional)
                - "vaccine" (dict with "expiration_date": datetime.date)
                - "wearing_a_mask" (bool)

        Returns:
            str: "Welcome to {cafe.name}" when all checks pass.

        Raises:
            NotVaccinatedError: If vaccine info is missing
                or expiration date missing.
            OutdatedVaccineError: If vaccine expiration_date is before today.
            NotWearingMaskError: If visitor is not wearing a mask.
        """
        visitor_name = visitor.get("name", "Unknown")
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"Visitor {visitor_name} is not vaccinated"
            )

        vaccine = visitor["vaccine"]
        expiration = vaccine.get("expiration_date")
        if expiration is None:
            raise NotVaccinatedError(
                f"Visitor {visitor_name} "
                f"has no vaccine expiration date"
            )

        if expiration < datetime.date.today():
            raise OutdatedVaccineError(
                f"Visitor {visitor_name}'s "
                f"vaccine expired on {expiration}"
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"Visitor {visitor_name} "
                f"is not wearing a mask"
            )

        return f"Welcome to {self.name}"
