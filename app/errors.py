class VaccineError(Exception):
    """Parent class for all vaccines errors"""


class NotWearingMaskError(Exception):
    """All visitors must wear masks"""


class OutdatedVaccineError(VaccineError):
    """All visitors vaccine should be not outdated"""


class NotVaccinatedError(VaccineError):
    """All visitors should be vaccinated"""
