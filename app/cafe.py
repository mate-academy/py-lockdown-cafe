from datetime import date

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    """
    Represents a cafe where visitors must meet certain health requirements
    (vaccination and mask-wearing) to be allowed entry.

    Attributes:
        name (str): The name of the cafe.
    """

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        """
        Checks if the visitor is allowed to visit the cafe
        based on their vaccination status, vaccine expiration date,
        and whether they are wearing a mask.

        Args:
            visitor (dict):
                A dictionary containing information about the visitor.
                Must include keys for 'vaccine' (with an 'expiration_date')
                and 'wearing_a_mask'.

        Raises:
            NotVaccinatedError: If the visitor does not have a vaccine.
            OutdatedVaccineError: If the visitor's vaccine has expired.
            NotWearingMaskError: If the visitor is not wearing a mask.

        Returns:
            str: A welcome message if the visitor meets all the requirements.
        """

        if "vaccine" not in visitor:
            raise NotVaccinatedError("Vaccine is needed")

        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Your vaccine is expired")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Mask wearing is needed")

        return f"Welcome to {self.name}"
