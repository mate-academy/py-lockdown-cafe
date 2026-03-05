import datetime
from .errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    """
    Represents a cafe with quarantine protocols.

    Attributes:
        name (str): the name of the establishment.
    """
    def __init__(
        self,
        name: str
    ) -> None:
        self.name = name

    def visit_cafe(
        self,
        visitor: dict
    ) -> str:
        """
        Processes a visitor's entry into the café.

        Args:

            visitor(dict): Dictionary with the visitor's data, including
            'name', 'vaccine', and 'wearing_a_mask'.

        Returns:

            str: A welcome message if all requirements are met.

        Raises:

            NotVaccinatedError: If the visitor has no vaccination record.

            OutdatedVaccineError: If the vaccination has expired.

            NotWearingMaskError: If the visitor is not wearing a mask.
        """
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor does not have a vaccine record.")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine has expired.")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        return f"Welcome to {self.name}"
