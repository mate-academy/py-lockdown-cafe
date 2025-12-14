# app/errors.py


class VaccineError(Exception):
    """Базовий клас для помилок, пов'язаних з вакциною."""
    pass


class NotVaccinatedError(VaccineError):
    """Якщо відвідувач не вакцинований."""

    def __init__(self, message: str = "Visitor is not vaccinated") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    """Якщо вакцина прострочена."""

    def __init__(self, message: str = "Vaccine is outdated") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    """Якщо відвідувач без маски."""

    def __init__(self, message: str = "Visitor is not wearing a mask") -> None:
        super().__init__(message)
