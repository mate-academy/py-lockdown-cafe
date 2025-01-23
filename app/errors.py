class VaccineError(Exception):
    """Базовий клас для помилок, пов'язаних із вакцинами."""
    pass

class NotVaccinatedError(VaccineError):
    """Помилка: відвідувач не щеплений."""
    pass

class OutdatedVaccineError(VaccineError):
    """Помилка: вакцина прострочена."""
    pass

class NotWearingMaskError(Exception):
    """Помилка: відвідувач не носить маску."""
    pass
