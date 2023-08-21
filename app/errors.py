class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "The visitor should be vaccinated."


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "The vaccination must be up to date."


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "The visitor should wear a mask."
