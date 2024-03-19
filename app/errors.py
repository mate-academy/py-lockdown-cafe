class VaccineError(Exception):
    def __str__(self) -> str:
        return "Visitor hasn't a valid vaccination"


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Visitor has no mask"
