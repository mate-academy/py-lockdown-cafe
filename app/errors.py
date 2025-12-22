class VaccineError(Exception):
    """Базовый класс для ошибок, связанных c вакциной."""
    pass


class NotVaccinatedError(VaccineError):
    """Ошибка: посетитель не вакцинирован."""
    pass


class OutdatedVaccineError(VaccineError):
    """Ошибка: вакцина просрочена."""
    pass


class NotWearingMaskError(Exception):
    """Ошибка: посетитель без маски."""
    pass
