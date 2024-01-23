class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):

    def __str__(self) -> str:
        return "Cannot access without a vaccine"


class OutdatedVaccineError(VaccineError):

    def __str__(self) -> str:
        return "Cannot access with an outdated vaccine"


class NotWearingMaskError(Exception):

    def __str__(self) -> str:
        return "Cannot access without mask"
