class VaccineError(Exception):
    """Parent class for vaccine-related errors"""


class NotVaccinatedError(VaccineError):
    """Get vaccine!"""


class OutdatedVaccineError(VaccineError):
    """Renew your vaccine!"""


class NotWearingMaskError(Exception):
    """Wear your mask or fuck off"""
