class VaccineError(Exception):
    """Base class for exceptions connected to vaccination"""
    pass


class NotVaccinatedError(VaccineError):
    """Called when the visitor has no information about the vaccine."""
    pass


class OutdatedVaccineError(VaccineError):
    """Called when the visitor's vaccine has expired."""
    pass


class NotWearingMaskError(Exception):
    """Called when a visitor does not have a mask or is not wearing it."""
    pass
