class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    """All visitors should be vaccinated"""


class OutdatedVaccineError(VaccineError):
    """The vaccine must not be expired"""


class NotWearingMaskError(Exception):
    """All visitors must wear masks"""
