class VaccineError(Exception):
    """All friends should be vaccinated"""


class NotVaccinatedError(VaccineError):
    """Error! The visitor doesn`t have vaccine"""


class OutdatedVaccineError(VaccineError):
    """Error! The visitor`s vaccine is outdated"""


class NotWearingMaskError(Exception):
    """Error! The visitor doesn't wear a mask"""
