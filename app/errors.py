class VaccineError(Exception):
    """VaccineError class exception"""


class NotVaccinatedError(VaccineError):
    """NotVaccinatedError VaccineError exception"""

    def __str__(self) -> str:
        return "Not Vaccinated Error"


class OutdatedVaccineError(VaccineError):
    """OutdatedVaccineError class exception"""

    def __str__(self) -> str:
        return "Outdated Vaccine Error"


class NotWearingMaskError(Exception):
    """NotWearingMaskError class exception"""

    def __str__(self) -> str:
        return "Not Wearing Mask Error"
