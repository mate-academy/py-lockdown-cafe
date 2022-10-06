class VaccineError(Exception):
    def __str__(self) -> str:
        return "All friends should be vaccinated"


class NotVaccinatedError(VaccineError):
    """NotVaccinatedError"""


class OutdatedVaccineError(VaccineError):
    """OutdatedVaccineError"""


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Friends should buy"
