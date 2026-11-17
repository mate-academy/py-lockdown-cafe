class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    """Raises an error if the visitor is unvaccinated."""
    def __str__(self) -> str:
        return "Sorry, but you are unvaccinated!"


class OutdatedVaccineError(VaccineError):
    """Raised if the vaccine in expired"""
    def __str__(self) -> str:
        return "Sorry, but you vaccine is expired!"


class NotWearingMaskError(Exception):
    """Raised if the visitor is not wearing mask"""
    def __str__(self) -> str:
        return "Sorry, but you are not wearing a mask!"
