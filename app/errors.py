class VaccineError(Exception):
    """Base class for other exceptions"""
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, message: str = "Person is not vaccinated") -> None:
        self.message = message
        super().__init__(self.message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message: str = "Vaccine is outdated") -> None:
        self.message = message
        super().__init__(self.message)


class NotWearingMaskError(Exception):
    def __init__(self, message: str = "Person is not wearing a mask") -> None:
        self.message = message
        super().__init__(self.message)
