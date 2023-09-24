class NotWearingMaskError(Exception):
    """Checks if client wears a mask."""


class VaccineError(Exception):
    """Parent exception for vaccine-related errors."""


class NotVaccinatedError(VaccineError):
    """Checks if client has vaccination certificate."""


class OutdatedVaccineError(VaccineError):
    """Checks if vaccination certificate hasn't expired."""
