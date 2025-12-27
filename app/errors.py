# errors.py
from __future__ import annotations

import datetime


class VaccineError(Exception):
    """Base class for vaccine-related errors."""


class NotVaccinatedError(VaccineError):
    """Visitor has no 'vaccine' data."""


class OutdatedVaccineError(VaccineError):

    def __init__(self, expiration_date: datetime.date) -> None:
        self.expiration_date = expiration_date
        super().__init__("Vaccine is outdated")


class NotWearingMaskError(Exception):
    """Visitor does not wear a mask."""
