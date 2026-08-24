class VaccineError(Exception):
    """Базовий виняток для помилок, пов'язаних із вакцинацією."""
    pass


class NotVaccinatedError(VaccineError):
    """Викликається, якщо у відвідувача відсутня вакцина."""
    pass


class OutdatedVaccineError(VaccineError):
    """Викликається, якщо термін дії вакцини закінчився."""
    pass


class NotWearingMaskError(Exception):
    """Викликається, якщо відвідувач не носить маску."""
    pass
