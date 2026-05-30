class VaccineError(Exception):
    """The basic exception for all vaccination issues."""
    pass


class NotVaccinatedError(VaccineError):
    """Called if the visitor does not have the 'vaccine' key at all."""
    pass


class OutdatedVaccineError(VaccineError):
    """Called if the vaccine has expired."""
    pass


class NotWearingMaskError(Exception):
    """Called if the visitor is not wearing a mask."""
    pass
