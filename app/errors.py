class VaccineError(Exception):
    def __str__(self) -> str:
        return "Visitor is not vaccinated"


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Visitor is not wearing a mask"
