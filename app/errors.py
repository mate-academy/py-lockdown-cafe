class VaccineError(Exception):
    """Base exception for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    pass
