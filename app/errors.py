class VaccineError(Exception):
    """
    Exception, which will be raised,
    if visitor has problem with vaccination
    """


class NotVaccinatedError(VaccineError):
    """
    Exception, which will be raised,
    if visitor doesn't have vaccination
    """


class OutdatedVaccineError(VaccineError):
    """
    Exception, which will be raised,
    if visitor has outdated vaccination
    """


class NotWearingMaskError(Exception):
    """
    Exception, which will be raised,
    if visitor doesn't have mask
    """
