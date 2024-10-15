class VaccineError(Exception):
    """
    parent vaccine error
    """


class NotVaccinatedError(VaccineError):
    """
    not vaccinated
    """


class OutdatedVaccineError(VaccineError):
    """
    outdated vaccine
    """


class NotWearingMaskError(Exception):
    """
    no mask
    """
