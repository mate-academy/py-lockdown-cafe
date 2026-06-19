class VaccineError(Exception):
    def __init__(self, message: str = "Vaccine error") -> None:
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    def __init__(self) -> None:
        super().__init__("Visitor is not vaccinated")


class OutdatedVaccineError(VaccineError):
    def __init__(self) -> None:
        super().__init__("Vaccine has expired")


class NotWearingMaskError(Exception):
    def __init__(self) -> None:
        super().__init__("Visitor is not wearing a mask")
