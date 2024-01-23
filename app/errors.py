class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return f"{self.__class__.__name__}"


class VaccineError(Exception):
    def __str__(self) -> str:
        return f"{self.__class__.__name__}"


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return super().__str__()


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return super().__str__()
