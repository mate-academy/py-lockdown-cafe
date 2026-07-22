class VaccineError(Exception):
    """Базовий клас для помилок, пов’язаних із вакцинацією."""


class NotVaccinatedError(VaccineError):
    """Відвідувач не має вакцинації."""


class OutdatedVaccineError(VaccineError):
    """Вакцина відвідувача прострочена."""


class NotWearingMaskError(Exception):
    """Відвідувач не носить маску."""
