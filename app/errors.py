class VaccineError(Exception):
    def __init__(self, message: str = "Visitor should be vaccinated") -> None:
        self.message = message
        super().__init__(self.message)


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    def __init__(self, message: str = "Visitor is not wearing a mask") -> None:
        self.message = message
        super().__init__(self.message)
