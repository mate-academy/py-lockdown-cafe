class VaccineError(Exception):
    def __str__(self) -> str:
        return "VaccineError"


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "NotVaccinatedError"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "OutdatedVaccineError"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "NotWearingMaskError"
