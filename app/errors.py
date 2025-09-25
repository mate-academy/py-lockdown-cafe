class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, name: str) -> None:
        self.message = f"Visitor {name} is not vaccinated"

    def __str__(self) -> str:
        return self.message


class OutdatedVaccineError(VaccineError):
    def __init__(self, name: str) -> None:
        self.message = f"Visitor {name} has an outdated vaccine"

    def __str__(self) -> str:
        return self.message


class NotWearingMaskError(Exception):
    def __init__(self, name: str) -> None:
        self.message = f"Visitor {name} is not wearing mask"

    def __str__(self) -> str:
        return self.message
