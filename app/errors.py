class VaccineError(Exception):
    """Parent class for all vaccine errors."""


class NotVaccinatedError(VaccineError):
    """Occurs when the visitor has not been vaccinated at all."""


class OutdatedVaccineError(VaccineError):
    """Occurs when visitor's has been outdated."""


class NotWearingMaskError(Exception):
    """Occurs when the visitor has not worn the mask."""
