class NotWearingMaskError(Exception):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Warning! {self.name} must wear the mask!"


class VaccineError(Exception):
    def __init__(self, name: str) -> None:
        self.name = name


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return f"Warning! {self.name} has no vaccine!"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return f"Warning! {self.name}`s vaccine is outdated!"
