class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "no vaccine"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "out dated vaccine"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "no mask"
