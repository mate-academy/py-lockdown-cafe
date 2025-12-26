class VaccineError(Exception):
    """class for errors"""


class NotVaccinatedError(VaccineError):
    """Exception raised when a visitor is not vaccinated."""
    def __str__(self) -> str:
        return "Visitor is not vaccinated."


class OutdatedVaccineError(VaccineError):
    """Exception raised when a visitor's vaccine is expired."""
    def __str__(self) -> str:
        return "Visitor's vaccine is outdated."


class NotWearingMaskError(Exception):
    """Exception raised when a visitor is not wearing a mask."""
    def __str__(self) -> str:
        return "Visitor is not wearing a mask."
