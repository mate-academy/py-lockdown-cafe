"""
Custom exceptions for the cafe application.

This module defines:
- VaccineError: base class for vaccine-related errors.
- NotVaccinatedError: raised when a visitor has no vaccine information.
- OutdatedVaccineError: raised when a visitor's vaccine is expired.
- NotWearingMaskError: raised when a visitor is not wearing a mask.

Each exception should be raised with a descriptive message from the caller,
e.g. "Visitor Paul is not vaccinated" or "Visitor Paul's
vaccine expired on 2022-01-01".
"""

__all__ = [
    "VaccineError",
    "NotVaccinatedError",
    "OutdatedVaccineError",
    "NotWearingMaskError",
]


class VaccineError(Exception):
    """Base class for vaccine-related errors.

    Use this to catch all vaccine problems (missing or outdated)
    in one except block.
    """


class NotVaccinatedError(VaccineError):
    """Raised when a visitor does not have vaccine information.

    Example message: "Visitor Paul is not vaccinated"
    """


class OutdatedVaccineError(VaccineError):
    """Raised when a visitor's vaccine is expired.

    Example message: "Visitor Paul's vaccine expired on 2022-01-01"
    """


class NotWearingMaskError(Exception):
    """Raised when a visitor is not wearing a mask.

    Example message: "Visitor Paul is not wearing a mask"
    """
