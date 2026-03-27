class VaccineError(Exception):
    """Parent class for vaccine errors"""


class NotVaccinatedError(VaccineError):
    """Raise when people haven't vaccine"""


class OutdatedVaccineError(VaccineError):
    """Raise when people have vaccine, but time of vaccine was expired."""


class NotWearingMaskError(Exception):
    """Raise when people haven't the mask"""
