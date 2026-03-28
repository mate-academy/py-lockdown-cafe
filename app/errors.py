class VaccineError(Exception):
    """
    Base Error for NotVaccinatedError and
            OutdatedVaccineError
    """


class NotWearingMaskError(Exception):
    """Mask mode!"""


class NotVaccinatedError(VaccineError):
    """Error: A man without a mask!"""


class OutdatedVaccineError(VaccineError):
    """The vaccine has expired!"""
