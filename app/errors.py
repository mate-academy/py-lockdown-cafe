"""
errors.py

This module defines custom exceptions used by the cafe lockdown checks.
"""


class VaccineError(Exception):
    """Base exception for all vaccine-related problems."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when a visitor has no vaccine record at all."""
    pass


class OutdatedVaccineError(VaccineError):
    """Raised when a visitor's vaccine has expired."""
    pass


class NotWearingMaskError(Exception):
    """Raised when a visitor is not wearing a mask."""
    pass
