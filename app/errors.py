class VaccineError(Exception):
    """VaccineError Exception"""


class NotVaccinatedError(VaccineError):
    """NotVaccinatedError Exception"""


class OutdatedVaccineError(VaccineError):
    """OutdatedVaccineError Exception"""


class NotWearingMaskError(Exception):
    """NotWearingMaskError Exception"""
