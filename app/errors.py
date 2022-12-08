class VaccineError(Exception):
    """Parent class for vaccine errors"""

    def __str__(self) -> str:
        return "All friends should be vaccinated"


class NotWearingMaskError(Exception):
    """Don't have a mask"""

    def __str__(self) -> str:
        return "NotWearingMaskError"


class NotVaccinatedError(VaccineError):
    """"No vaccine"""


class OutdatedVaccineError(VaccineError):
    """Outdated vaccine"""
