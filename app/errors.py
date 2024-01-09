class VaccineError(Exception):
    pass


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "OutdatedVaccineError"


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "NotVaccinatedError"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "NotWearingMaskError"
