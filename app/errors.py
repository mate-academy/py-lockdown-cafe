class VaccineError(Exception):
    """General error for the vaccination"""
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


class NotVaccinatedError(VaccineError):
    """Human not vaccinated error"""


class OutdatedVaccineError(VaccineError):
    """Error when human has an outdated vaccine"""


class NotWearingMaskError(Exception):
    """Error when human is not wearing mask"""
