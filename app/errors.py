class VaccineError(Exception):
    def __init__(self, name: str, message: str) -> None:
        self.name = name
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    def __init__(self, name: str) -> None:
        message = f"{name} is not vaccinated"
        super().__init__(name, message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, name: str) -> None:
        message = f"{name} has an outdated vaccine"
        super().__init__(name, message)


class NotWearingMaskError(Exception):
    def __init__(self, name: str) -> None:
        message = f"{name} is not wearing a mask"
        super().__init__(message)
