class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, message: str = "All friends should be vaccinated")\
            -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message: str = "All friends should be vaccinated")\
            -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    pass
