class VaccineError(Exception):
    """problems with vaccine"""


class NotVaccinatedError(VaccineError):
    """not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """outdated vaccines"""


class NotWearingMaskError(Exception):
    """Are you kidding? It's 2023"""
