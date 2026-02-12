class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    """NotVaccinatedError"""


class OutdatedVaccineError(VaccineError):
    """Vaccine expired"""


class NotWearingMaskError(Exception):
    """You should wear a mask"""
