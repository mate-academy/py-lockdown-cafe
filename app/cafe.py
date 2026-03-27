"""
This module defines the Cafe class, which represents a cafe that can be
visited by visitors.
"""
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    """
    Represents a cafe with a name that can be visited by people.
    """
    def __init__(self, name: str) -> None:
        """
        Initializes a Cafe object.

        :param name: The name of the cafe.
        :type name: str
        """
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        """
        Simulates a visitor visiting the cafe.

        This method checks if the visitor meets the requirements to enter the
        cafe. If the visitor is not vaccinated, has an outdated vaccine, or is
        not wearing a mask, an exception is raised. Otherwise, a welcome
        message is returned.

        :param visitor: A dictionary representing the visitor.
        :type visitor: dict
        :return: A welcome message.
        :rtype: str
        :raises NotVaccinatedError: If the visitor is not vaccinated.
        :raises OutdatedVaccineError: If the visitor's vaccine is outdated.
        :raises NotWearingMaskError: If the visitor is not wearing a mask.
        """
        for error in (
            NotVaccinatedError,
            OutdatedVaccineError,
            NotWearingMaskError,
        ):
            error.check(visitor)

        return f"Welcome to {self.name}"
