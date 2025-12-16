class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    """NotVaccinatedError"""


class OutdatedVaccineError(VaccineError):
    """OutdatedVaccineError"""


class NotWearingMaskError(Exception):
    """NotWearingMaskError"""
