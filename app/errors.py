class VaccineError(Exception):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return (f"Friend {self.name} doesn't have vaccine"
                f" or vaccine is outdated.")


class NotVaccinatedError(VaccineError):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Friend {self.name} doesn't have vaccine"


class OutdatedVaccineError(VaccineError):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Friend {self.name} has outdated vaccine."


class NotWearingMaskError(Exception):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Friend {self.name} doesn't have a mask."
