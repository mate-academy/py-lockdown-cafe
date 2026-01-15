class VaccineError(Exception):
    """Base class for vaccination-related errors."""


class NotVaccinatedError(VaccineError):
    def __init__(self, name: str) -> None:
        super().__init__(f"{name} is not vaccinated!")


class OutdatedVaccineError(VaccineError):
    def __init__(self, name: str) -> None:
        super().__init__(f"{name}'s vaccine is outdated!")


class NotWearingMaskError(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(f"{name} is not wearing a mask!")
