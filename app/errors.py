class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    """
    """


class OutdatedVaccineError(VaccineError):
    """
    """


class NotWearingMaskError(Exception):
    """
    """
