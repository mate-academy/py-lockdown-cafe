class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    """
    visitor dont have vaccination
    """


class OutdatedVaccineError(VaccineError):
    """
    vaccine ist expire
    """


class NotWearingMaskError(Exception):
    """
    visitor dont have a mask
    """
