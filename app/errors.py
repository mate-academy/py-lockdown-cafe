class VaccineError(Exception):
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {super().__str__()}"


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {super().__str__()}"
