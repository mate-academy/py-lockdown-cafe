class VaccineError(Exception):

    def __str__(self) -> str:
        return "Visitor should be vaccinated"


class NotVaccinatedError(VaccineError):

    def __str__(self) -> str:
        return super().__str__()


class OutdatedVaccineError(VaccineError):

    def __str__(self) -> str:
        return super().__str__()


class NotWearingMaskError(Exception):

    def __str__(self) -> str:
        return "Visitor must have a mask"
