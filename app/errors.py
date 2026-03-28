class VaccineError(Exception):
    """Error is raised when visitor has some problems with vaccine"""


class NotVaccinatedError(VaccineError):
    """Error is raised when visitor doesn't have vaccine"""
    def __init__(self) -> None:
        super().__init__("Some of visitors are not vaccinated")


class OutdatedVaccineError(VaccineError):
    """Error is raised when visitor has outdated vaccine"""
    def __init__(self) -> None:
        super().__init__("Some of visitors have outdated vaccine")


class NotWearingMaskError(Exception):
    """Error is raised when visitor doesn't wear a mask"""
    def __init__(self) -> None:
        super().__init__("Some of visitors don't have a mask")
