class VaccineError(Exception):
    """VaccineError"""


class OutdatedVaccineError(VaccineError):
    """OutdatedVaccineError"""


class NotVaccinatedError(VaccineError):
    """NotVaccinatedError"""


class NotWearingMaskError(Exception):
    """NotWearingMaskError"""
