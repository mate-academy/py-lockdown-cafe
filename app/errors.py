class VaccineError(Exception):
    """Базовий клас для проблем з вакциною"""
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, message: str = "Visitor must be vaccinated") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message: str = "Vaccine has expired") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self, message: str = "Visitor must wear a mask") -> None:
        super().__init__(message)
