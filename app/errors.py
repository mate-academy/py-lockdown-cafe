class VaccineError(Exception):
    """Base class for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Exception raised when a visitor is not vaccinated."""
    def __init__(self) -> None:
        super().__init__("Visitor is not vaccinated")


class OutdatedVaccineError(VaccineError):
    """Exception raised when a visitor's vaccine is expired"""
    def __init__(self) -> None:
        super().__init__("Visitor's vaccine is outdated")


class NotWearingMaskError(Exception):
    """Exception raised when a visitor is not wearing a mask"""
    def __init__(self) -> None:
        super().__init__("Visitor is not wearing a mask")
