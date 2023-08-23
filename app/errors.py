class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Visitor must be vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "The vaccine has expired"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "The visitor must wear a mask"
