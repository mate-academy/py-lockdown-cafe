class VaccineError(Exception):
    def __str__(self) -> str:
        return "You should get vaccinated"


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "You should buy mask"
