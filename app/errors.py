class VaccineError(Exception):
    """Base class for vaccine errors"""


class NotVaccinatedError(VaccineError):
    """No vaccine certificate were provided"""


class OutdatedVaccineError(VaccineError):
    """Vaccine certificate is outdated"""


class NotWearingMaskError(Exception):
    """Mask location is unknown, but, for sure, it is not at your face"""
