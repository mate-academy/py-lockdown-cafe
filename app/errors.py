class VaccineError(Exception):
    def __str__(self) -> str:
        return "Not vaccine"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "The visitor does not wear a mask"


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "If the visitor does not have a vaccine key"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Expired vaccine"
