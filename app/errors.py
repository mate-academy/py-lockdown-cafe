class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Visitor not vaccinated."


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Visitor vaccine is outdated."


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Visitor is not wearing a mask."
