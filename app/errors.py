class VaccineError(Exception):
    pass


class NotWearingMaskError(Exception):
    def __init__(self, name: str) -> None:
        self.name = name
        super().__init__(f"{self.name} should be in mask")


class NotVaccinatedError(VaccineError):
    def __init__(self, name: str) -> None:
        self.name = name
        super().__init__(f"{self.name} is not vaccinated.")


class OutdatedVaccineError(VaccineError):
    def __init__(self, name: str) -> None:
        self.name = name
        super().__init__(f"{self.name} has an outdated vaccine.")
