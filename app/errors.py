class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "You should be vaccinated to visit our cafe"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Sorry, the visitor's vaccine is outdated"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Only visitors wearing masks allowed"
