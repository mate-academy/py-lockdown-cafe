class VaccineError(Exception):
    """any vaccine of troubles"""


class NotVaccinatedError(VaccineError):
    """no vaccination key found"""


class OutdatedVaccineError(VaccineError):
    """vaccine expired"""


class NotWearingMaskError(Exception):
    """visitor must wear mask"""
