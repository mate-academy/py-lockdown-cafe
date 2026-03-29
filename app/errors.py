class NotWearingMaskError(Exception):
    """
    If guest didn't wear mask
    """
    pass


class VaccineError(Exception):
    """
    If guest hasn't relevant vaccine
    """
    pass


class NotVaccinatedError(VaccineError):
    """
    If guest didn't do vaccine
    """
    pass


class OutdatedVaccineError(VaccineError):
    """
    If time of vaccine is out
    """
    pass
