class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "NotVaccinatedError. Visitor is not vaccinated."


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "OutdatedVaccineError. Visitor's vaccine is outdated."


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "NotWearingMaskError. Visitor is not wearing a mask."
