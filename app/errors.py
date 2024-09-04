class VaccineError(Exception):
    pass


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "NotWearingMaskError"


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "NotVaccinatedError"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "OutdatedVaccineError"
