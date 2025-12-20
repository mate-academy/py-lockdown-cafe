class VaccineError(Exception):
    def __init__(self, name: str) -> None:
        self.name = name


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return f"{self.name} don't have a vaccine!"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return f"{self.name}'s vaccine expired!"


class NotWearingMaskError(Exception):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"{self.name} without a mask!"
