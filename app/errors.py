class VaccineError(Exception):
    """Базовый класс для ошибок, связанных с вакцинацией."""
    pass


class NotVaccinatedError(VaccineError):
    """Исключение, возникающее, когда посетитель не вакцинирован."""
    def __init__(self,
                 message: str = "Visitor is not vaccinated.") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    """Исключение, возникающее, когда вакцина просрочена."""
    def __init__(self,
                 message: str = "Visitor's vaccine is outdated.") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    """Исключение, возникающее, когда посетитель не носит маску."""
    def __init__(self,
                 message: str = "Visitor is not wearing a mask.") -> None:
        super().__init__(message)
