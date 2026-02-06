class VaccineError(Exception):
    """Check vaccinate and outdated"""


class NotVaccinatedError(VaccineError):
    """Check vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Check date  of vaccine"""


class NotWearingMaskError(Exception):
    """Check mask visitor"""
