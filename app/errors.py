class VaccineError(Exception):
    """Raised when the visitor isn't vaccinated or their vaccine is expired"""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when the visitor isn't vaccinated"""

    def __str__(self) -> str:
        return "Sorry, you can't visit the cafe! You aren't vaccinated!"


class OutdatedVaccineError(VaccineError):
    """Raised when the visitor's vaccine is expired"""

    def __str__(self) -> str:
        return "Sorry, you can't visit the cafe! Your vaccine is expired!"


class NotWearingMaskError(Exception):
    """Raised when the visitor isn't wearing a mask"""

    def __str__(self) -> str:
        return "Sorry, you can't visit the cafe! You aren't wearing a mask!"
