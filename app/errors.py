class NotWearingMaskError(Exception):
    """
    raise when the visitor does not have a mask
    """


class VaccineError(Exception):
    """
    raise when visitor can not visit the cafe.
    """


class NotVaccinatedError(VaccineError):
    """
    raise when visitor is not vaccinated
    """


class OutdatedVaccineError(VaccineError):
    """
    raise when the vaccine is expired
    """
