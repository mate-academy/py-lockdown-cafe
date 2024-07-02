class VaccineError(Exception):
    def __init__(self) -> None:
        self.message = "Person should be vaccinated"
        super().__init__(self.message)


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    def __init__(self) -> None:
        self.message = "Person should wear a mask"
        super().__init__(self.message)
