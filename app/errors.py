class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Visitor is not vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Visitor's vaccine is expired"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Visitor is not wearing a mask"
