class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "You need a vaccine"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Your vaccine is expire."


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Visitors need a mask"
