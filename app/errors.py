class VaccineError(Exception):
    """Vaccination problem"""


class NotVaccinatedError(VaccineError):
    """Not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Outdated vaccination"""


class NotWearingMaskError(Exception):
    """No mask"""
