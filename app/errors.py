class VaccineError(Exception):
    """Our VaccineError exception"""


class NotVaccinatedError(VaccineError):
    """Our NotVaccinatedError exception"""


class OutdatedVaccineError(VaccineError):
    """Our OutdatedVaccineError exception"""


class NotWearingMaskError(Exception):
    """Our NotWearingMaskError exception"""
