class VaccineError(Exception):
    def __str__(self) -> str:
        return "All friends should be vaccinated"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Visitor have to wear a mask"


class NotVaccinatedError(VaccineError):
    """"No vaccine"""


class OutdatedVaccineError(VaccineError):
    """Outdated vaccine"""
