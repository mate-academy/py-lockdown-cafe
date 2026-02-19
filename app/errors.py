class VaccineError(Exception):
    """Базовий клас для помилок, пов'язаних з вакцинацією"""
    pass


class NotVaccinatedError(VaccineError):
    """Виняток для невакцинованих відвідувачів"""
    pass


class OutdatedVaccineError(VaccineError):
    """Виняток для прострочених вакцин"""
    pass


class NotWearingMaskError(Exception):
    """Виняток для відвідувачів без маски"""
    pass
