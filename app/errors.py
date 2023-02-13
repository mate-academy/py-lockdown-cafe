class VaccineError(Exception):
    """Exception parent class"""


class NotVaccinatedError(VaccineError):
    """Exception if visitor don`t have vaccination key"""


class OutdatedVaccineError(VaccineError):
    """Exception if vaccination key is outdated"""


class NotWearingMaskError(Exception):
    """Exception if visitor don`t have wearing mask"""
