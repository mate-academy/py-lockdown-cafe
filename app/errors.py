class VaccineError(Exception):
    """Occurs when there is a vaccination error"""


class NotVaccinatedError(VaccineError):
    """Occurs when you have not done any vaccinations"""


class OutdatedVaccineError(VaccineError):
    """Occurs when a vaccine is outdated"""


class NotWearingMaskError(Exception):
    """Occurs when you are without mask"""
