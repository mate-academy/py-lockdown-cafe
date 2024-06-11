class NotVaccinatedError(Exception):
    """The visitor has no vaccine"""

class OutdatedVaccineError(Exception):
    """Old vaccine"""

class NotWearingMaskError(Exception):
    """All visitors must wear a mask"""
