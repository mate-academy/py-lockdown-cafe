class VaccineError(Exception):
    def __str__(self) -> str:
        pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "You should get vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "You should get a new vaccine"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "You should buy mask"
