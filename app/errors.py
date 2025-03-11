class VaccineError(Exception):
    pass


class NotWearingMaskError(Exception):
    """Our NotWearingMaskError Exception"""


class NotVaccinatedError(VaccineError):
    """Our NotVaccinatedError Exception"""


class OutdatedVaccineError(VaccineError):
    """Our OutdatedVaccineError Exception"""
