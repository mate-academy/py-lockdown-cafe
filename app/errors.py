class VaccineError(Exception):
    def __str__(self) -> str:
        return "All friends should be vaccinated"


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Every visitor has to be vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "All visitors must have correct data vaccine"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "All visitors must wear masks"
