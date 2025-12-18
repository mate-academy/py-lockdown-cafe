class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, name: str) -> None:
        super().__init__(f"{name} is not vaccinated!")


class OutdatedVaccineError(VaccineError):
    def __init__(self, name: str) -> None:
        super().__init__(f"{name} has an outdated vaccine!")


class NotWearingMaskError(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(f"{name} is not wearing a mask!")
