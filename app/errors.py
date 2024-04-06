class VaccineError(Exception):
    """parent class for other errors"""


class NotVaccinatedError(VaccineError):
    """raised if a visitor is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """raised if a visitor has an outdated vaccine certificate"""


class NotWearingMaskError(Exception):
    """raised if a visitor does not wear a mask"""
