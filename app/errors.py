class NotWearingMaskError(Exception):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}, you need to wear the mask!"


class VaccineError(Exception):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"{self.name} need a valid vaccination!"


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return f"{self.name} has to be vaccinated!"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return f"{self.name}, your vaccination is expired!"
