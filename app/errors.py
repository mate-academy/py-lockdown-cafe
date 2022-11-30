class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    """Visitors without vaccination."""


class OutdatedVaccineError(VaccineError):
    """If vaccination expired."""


class NotWearingMaskError(Exception):
    """If visitors are without a mask."""
