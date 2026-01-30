class VaccineError(Exception):
    def __init__(self, visitor_name: str) -> None:
        self.visitor_name = visitor_name


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return f"{self.visitor_name} is not vaccinated!"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return f"{self.visitor_name}'s vaccine is outdated!"


class NotWearingMaskError(Exception):
    def __init__(self, visitor_name: str) -> None:
        self.visitor_name = visitor_name

    def __str__(self) -> str:
        return f"{self.visitor_name} is not wearing a mask!"
