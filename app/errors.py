class VaccineError(Exception):
    """Custom exception for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Custom exception for non-vaccinated visitors."""
    pass


class OutdatedVaccineError(VaccineError):
    """Custom exception for visitors with outdated vaccines."""
    pass


class NotWearingMaskError(Exception):
    """Custom exception for visitors not wearing masks."""
    pass
