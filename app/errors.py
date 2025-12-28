class VaccineError(Exception):
    def __init__(self, name: str) -> None:
        self.name = name


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return f"The visitor {self.name} is not vaccinated!"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return f"The {self.name}'s vaccine has expired!"


class NotWearingMaskError(Exception):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"The visitor {self.name} doesn't wear a mask!"
