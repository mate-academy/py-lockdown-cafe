class VaccineError(Exception):
    """Error in case person has a problem with vaccine"""


class NotVaccinatedError(VaccineError):
    """Error in case person is not vaccinated"""
    def __init__(self, message: str = "Visitor is not vaccinated") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    """Error in case person has expired vaccine"""
    def __init__(self, message: str = "Vaccine is outdated") -> None:
        super().__init__(message)


class NotWearingMaskError (Exception):
    """Error in case person has expired vaccine"""
    def __init__(self, message: str = "Visitor is not wearing a mask") -> None:
        super().__init__(message)
