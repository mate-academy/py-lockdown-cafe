class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Not vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Outdated vaccine"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Not wearing a mask"
