class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Please, get a vaccine!"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Unfortunately, your vaccine is expire."


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Visitors should wear a mask."
