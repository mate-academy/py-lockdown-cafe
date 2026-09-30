class VaccineError(Exception):
    """Parent error exception"""


class NotVaccinatedError(VaccineError):
    """If the visitor does not have a vaccine key"""


class OutdatedVaccineError(VaccineError):
    """If the vaccine expiration date is expired"""


class NotWearingMaskError(Exception):
    """If at least one visitor does not wears a mask"""
