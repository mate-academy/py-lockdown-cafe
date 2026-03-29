class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, message: str = "Visitor is not vaccinated") -> None:
        self.message = message
        super().__init__(self.message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message: str = "Visitor's vaccine is outdated") -> None:
        self.message = message
        super().__init__(self.message)


class NotWearingMaskError(Exception):
    def __init__(self, message: str = "Visitor is not wearing a mask") -> None:
        self.message = message
        super().__init__(self.message)
