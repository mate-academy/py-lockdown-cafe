class VaccineError(Exception):
    """A visitor is not vaccinated or has outdated vaccine"""


class OutdatedVaccineError(VaccineError):
    """A visitor has outdated vaccine"""


class NotVaccinatedError(VaccineError):
    """A visitor is not vaccinated"""


class NotWearingMaskError(Exception):
    """A visitor is not wearing mask"""
