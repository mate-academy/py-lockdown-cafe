class VaccineError(Exception):
    """
    This exception is raised if a visitor is not vaccinated or has
    an expired vaccine.
    """


class NotVaccinatedError(VaccineError):
    """
    This exception is raised if a visitor is not vaccinated.
    """


class OutdatedVaccineError(VaccineError):
    """
    This exception is raised if a visitor's vaccine is expired.
    """


class NotWearingMaskError(Exception):
    """
    This exception is raised if a visitor does not wear a mask.
    """
