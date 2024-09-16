class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Sorry, the visitor should be vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Sorry, the vaccine is outdated"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Do not enter without mask"
