class NotWearingMaskError(Exception):
    """If visitor without mask"""
    pass


class VaccineError(Exception):
    """Exception about vaccine"""


class NotVaccinatedError(VaccineError):
    """If key vaccine not in dict"""


class OutdatedVaccineError(VaccineError):
    """if date vaccine < date.today"""
