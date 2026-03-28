class VaccineError(Exception):
    """Problem with vaccine"""


class NotVaccinatedError(VaccineError):
    """Not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Vaccine out of date"""


class NotWearingMaskError(Exception):
    """Have no mask"""
