class VaccineError(Exception):
    """Base class for all vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Exception raised when a visitor is not vaccinated."""

    def __init__(self, message: str = "Visitor is not vaccinated."
                                      " A vaccine key is required.") -> None:

        self.message = message
        super().__init__(self.message)


class OutdatedVaccineError(VaccineError):
    """Exception raised when a visitor's vaccine is outdated."""

    def __init__(self, message: str = "The visitor's vaccine has expired.")\
            -> None:
        self.message = message
        super().__init__(self.message)


class NotWearingMaskError(Exception):
    """Exception raised when a visitor is not wearing a mask."""

    def __init__(self, message: str = "Visitor is not wearing a mask.")\
            -> None:

        self.message = message
        super().__init__(self.message)
