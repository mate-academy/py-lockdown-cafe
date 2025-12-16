class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "You need to have a vaccination"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "You need to update ur vaccine"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Go wear mask! Buy it, whatever"
