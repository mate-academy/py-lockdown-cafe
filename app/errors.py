class VaccineError(Exception):
    """
    VaccineError
    """


class NotWearingMaskError(Exception):
    """
    NotWearingMaskError
    """


class NotVaccinatedError(VaccineError):
    """
    NotVaccinatedError
    """


class OutdatedVaccineError(VaccineError):
    """
    OutdatedVaccineError
    """
