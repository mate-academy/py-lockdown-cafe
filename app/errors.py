class VaccineError(Exception):
    """Raised if the visitor has a problem with vaccination"""


class NotVaccinatedError(VaccineError):
    """Raises if the visitor is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Raises when the visitor`s vaccine is out of date"""


class NotWearingMaskError(Exception):
    """Raises when the visitor is not wearing a mask"""
