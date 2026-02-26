class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "You are not vaccinated."


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Your vaccine is outdated."


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "You are not wearing a mask."
