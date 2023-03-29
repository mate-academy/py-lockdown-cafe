class VaccineError(Exception):
    """some explanation"""


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "NotWearingMaskError"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "OutdatedVaccineError"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "NotWearingMaskError"
