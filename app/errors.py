class VaccineError(Exception):
    """Common vaccine error"""


class NotVaccinatedError(VaccineError):
    """Check for stupid person"""


class OutdatedVaccineError(VaccineError):
    """Check is a person have plans for future"""


class NotWearingMaskError(Exception):
    """Check for people with big nose"""
