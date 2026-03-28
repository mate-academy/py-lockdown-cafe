# Модуль для кастомних винятків

class VaccineError(Exception):
    """Базовий клас для проблем із вакциною"""
    pass

class NotVaccinatedError(VaccineError):
    """Відсутня вакцина"""
    pass

class OutdatedVaccineError(VaccineError):
    """Прострочена вакцина"""
    pass

class NotWearingMaskError(Exception):
    """Відвідувач не носить маску"""
    pass
