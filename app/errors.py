class VaccineError(Exception):
    """
        Exception raised for errors related to vaccine operations.

        Attributes:
        message (str)
    """


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    pass
