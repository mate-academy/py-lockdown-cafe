class VaccineError(Exception):
    """Parent for vaccine errors"""


class NotVaccinatedError(VaccineError):
    """Raise when visitor has no 'vaccine' key"""


class OutdatedVaccineError(VaccineError):
    """Raise when visitors vaccine expired"""


class NotWearingMaskError(Exception):
    """Raise when visitor not wear mask"""
