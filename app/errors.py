class VaccineError(Exception):
    """All errors are related to vaccine"""


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "The visitor does not have a vaccine"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "The vaccine is expired"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "NotVaccinatedError should be raised with a message"
