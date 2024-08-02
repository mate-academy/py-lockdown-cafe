class VaccineError(Exception):

    def __str__(self) -> str:
        return "Visitor should be vaccinated"


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Visitor should buy a mask"
