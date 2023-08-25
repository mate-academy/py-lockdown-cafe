class VaccineError(Exception):
    def __init__(self,
                 message: str = "Problem with vaccine") -> None:
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    def __init__(self,
                 message: str = "Not vaccinated") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self,
                 message: str = "Outdated vaccine") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self,
                 message: str = "Not wearing mask") -> None:
        super().__init__(message)
