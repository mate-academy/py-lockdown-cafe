class VaccineError(Exception):
    """Some problem with vaccine"""


class NotVaccinatedError(VaccineError):
    """You are not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Vaccine outdated"""


class NotWearingMaskError(Exception):
    """Please wear a mask"""
