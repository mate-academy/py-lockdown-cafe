class VaccineError(Exception):
    """main vaccine error"""


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "The visitor does not have a vaccine"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "The visitor vaccine must not be expired"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "The visitor is not wearing a mask"
