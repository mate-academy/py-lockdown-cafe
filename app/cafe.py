"""
cafe.py

This module describes a cafe that enforces pandemic entry rules.
"""

import datetime

from app.errors import (NotVaccinatedError, OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    """Represents a cafe with pandemic entry requirements."""

    def __init__(self, name: str) -> None:
        """
        :param name: str, the name of the cafe.
        """
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        """
        Check whether a visitor is allowed to enter the cafe.

        :param visitor: dict, information about the visitor. May contain
            "name", "age", "vaccine" (with "expiration_date"), and
            "wearing_a_mask".
        :return: str, a welcome message if the visitor is allowed in.
        :raises NotVaccinatedError: if the visitor has no vaccine record.
        :raises OutdatedVaccineError: if the visitor's vaccine has expired.
        :raises NotWearingMaskError: if the visitor is not wearing a mask.
        """
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor['name']} is not vaccinated!"
            )

        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor['name']}'s vaccine is outdated!"
            )

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                f"{visitor['name']} is not wearing a mask!"
            )

        return f"Welcome to {self.name}"
