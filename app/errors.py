class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, message : str = "You are not vaccinated.") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message : str = "Your vaccine is outdated.") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self, message : str = "You are not wearing a mask.") -> None:
        super().__init__(message)
