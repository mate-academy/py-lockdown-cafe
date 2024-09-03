class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


class NotWearingMaskError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)
