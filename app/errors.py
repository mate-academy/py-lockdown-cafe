class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, message: str = "NotVaccinatedError") -> None:
        self.message = message
        super().__init__(self.message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message: str = "OutdatedVaccineError") -> None:
        self.message = message
        super().__init__(self.message)


class NotWearingMaskError(Exception):
    def __init__(self, message: str = "NotWearingMaskError") -> None:
        self.message = message
        super().__init__(self.message)
