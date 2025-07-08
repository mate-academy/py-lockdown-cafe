class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Visitor must be vaccinated to enter the cafe."


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Vaccine is outdated."


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Visitor must wear a mask."
