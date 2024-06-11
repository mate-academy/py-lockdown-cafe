class VaccineError(Exception):
    pass

class NotVaccinatedError(VaccineError):
    """The visitor has no vaccine"""

class OutdatedVaccineError(VaccineError):
    """Old vaccine"""

class NotWearingMaskError(Exception):
    """All visitors must wear a mask"""
