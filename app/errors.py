class VaccineError(Exception):
    """
    Base exception for errors related to vaccination
    status when entering the cafe.
    """


class NotVaccinatedError(VaccineError):
    """
    Raised when a visitor attempts to enter the cafe
    without proof of vaccination.
    """


class OutdatedVaccineError(VaccineError):
    """
    Raised when a visitor attempts to enter the cafe
    with proof of vaccination that is no longer valid
    because the vaccine has expired.
    """


class NotWearingMaskError(Exception):
    """
    Raised when a visitor attempts to enter the cafe
    without wearing a mask.
    """
