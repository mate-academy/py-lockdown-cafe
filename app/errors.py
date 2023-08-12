class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Visitor do not have vaccine"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Vaccine is expired"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "All visitors must wear masks"
