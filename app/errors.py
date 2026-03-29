class NotWearingMaskError(Exception):
    """Exception which will be raised if visitor doesn't wear a mask."""


class VaccineError(Exception):
    """Exception if visitor has problems with vaccine."""


class NotVaccinatedError(VaccineError):
    """Exception if visitor doesn't have a 'vaccine' key."""


class OutdatedVaccineError(VaccineError):
    """Exception if visitor's vaccine is expired."""
