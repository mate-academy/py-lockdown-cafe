class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self,
                 message: str = "All friends should be vaccinated") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self,
                 message: str = "One of friends has outdated vaccine") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self,
                 message: str = "Some friends are not wearing a mask") -> None:
        super().__init__(message)
