class VaccineError(Exception):
    """Parent Class for Vaccine Errors"""


class NotVaccinatedError(VaccineError):
    """The person is not vaccinated"""
    def __str__(self) -> str:
        return "Not Vaccinated"


class OutdatedVaccineError(VaccineError):
    """Duration of effectiveness of vaccination is expired"""
    def __str__(self) -> str:
        return "Expired vaccination duration"


class NotWearingMaskError(Exception):
    """The person without a mask"""
    def __str__(self) -> str:
        return "No mask - No coffee"
