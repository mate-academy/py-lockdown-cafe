class VaccineError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


class NotVaccinatedError(VaccineError):
    def __init__(self, message: str = "Not vaccinated") -> None:
        self.message = message
        super().__init__(self.message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message: str = "Vaccine is outdated") -> None:
        self.message = message
        super().__init__(self.message)


class NotWearingMaskError(Exception):
    def __init__(self, message: str = "Not wear mask") -> None:
        self.message = message
        super().__init__(self.message)
