class VaccineError(Exception):
    """Базовий клас для виключень, пов'язаних з вакцинацією."""
    pass


class NotVaccinatedError(VaccineError):
    """Виключення, яке викидається, коли відвідувач не вакцинований."""
    pass


class OutdatedVaccineError(VaccineError):
    """Виключення, яке викидається, коли вакцина застаріла."""
    pass


class NotWearingMaskError(Exception):
    """Виключення, яке викидається, коли відвідувач не носить маску."""
    pass
