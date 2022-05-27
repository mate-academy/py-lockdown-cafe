class VaccineError(Exception):
    """
    Father class for NotVaccinatedError &
    OutdatedVaccineError
    """


class NotVaccinatedError(VaccineError):
    """
    Error if visitor doesn't have a Vaccine
    """


class OutdatedVaccineError(VaccineError):
    """
    Error if visitor vaccine is outdated
    """


class NotWearingMaskError(Exception):
    """
    Error if visitor doesn't have a mask
    """
