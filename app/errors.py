class VaccineError(Exception):
    """That kind of exception is the parent
    to NotVaccinatedError and OutdatedVaccineError"""


class NotVaccinatedError(VaccineError):
    """Raised when a vaccine is unavailable"""


class OutdatedVaccineError(VaccineError):
    """Raised when a vaccine is outdated"""


class NotWearingMaskError(Exception):
    """That exception raised when client
    is not wearing the mask in the cafe"""
