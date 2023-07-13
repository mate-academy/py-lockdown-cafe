import datetime


class VaccineError(Exception):
    def __init__(self, name: str) -> None:
        self.name = name


class NotVaccinatedError(VaccineError):
    def __init__(self, name: str) -> None:
        super().__init__(name=name)

    def __str__(self) -> str:
        return f"Visitor {self.name} cannot enter the cafe because " \
            f"he doesn't have a vaccination."


class OutdatedVaccineError(VaccineError):
    current_date = datetime.date.today()

    def __init__(self, name: str) -> None:
        super().__init__(name=name)

    def __str__(self) -> str:
        return f"Visitor {self.name} cannot enter the cafe because " \
            f"his vaccination has expired."


class NotWearingMaskError(Exception):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Visitor {self.name} cannot enter the cafe because" \
            f"he does not have a medical mask"
