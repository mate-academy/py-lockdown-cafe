class VaccineError(Exception):
    """Person is not vaccinated or vaccine had expired"""


class NotVaccinatedError(VaccineError):
    """Person is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """The vaccine had expired"""


class NotWearingMaskError(Exception):
    """The visitor without mask"""
