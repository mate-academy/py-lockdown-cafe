class VaccineError(Exception):  # """Base class for vaccine-related errors"""
    pass


class NotVaccinatedError(VaccineError):  # if some not vaccine
    def __init__(self, name: str) -> None:
        self.message = f"Visitor {name} is not vaccinated"

    def __str__(self) -> str:
        return self.message


class OutdatedVaccineError(VaccineError):  # if vaccine outdate
    def __init__(self, name: str) -> None:
        self.message = f"Visitor {name} has an outdated vaccine"

    def __str__(self) -> str:
        return self.message


class NotWearingMaskError(Exception):  # if someone without mask
    def __init__(self, name: str) -> None:
        self.message = f"Visitor {name} is not wearing mask"

    def __str__(self) -> str:
        return self.message
