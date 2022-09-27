class VaccineError(Exception):
    """VaccineError"""
    def __str__(self):
        return "All friends should be vaccinated"


class NotVaccinatedError(VaccineError):
    """NotVaccinatedError"""


class OutdatedVaccineError(VaccineError):
    """OutdatedVaccineError"""


class NotWearingMaskError(Exception):
    def __str__(self):
        return "Friends should be in masks"
