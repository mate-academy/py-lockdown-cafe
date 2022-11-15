class VaccineError(Exception):
    """Exception parent class if vaccination is invalid"""
    def __str__(self) -> str:
        return "All friends should be vaccinated"


class NotVaccinatedError(VaccineError):
    """Exception if visitor have no vaccination key"""


class OutdatedVaccineError(VaccineError):
    """Exception if vaccination key is outdated"""


class NotWearingMaskError(Exception):
    """Exception if visitor is not wearing mask"""
    def __str__(self) -> str:
        return "Friends should buy masks"
