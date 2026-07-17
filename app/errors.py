class VaccineError(Exception):
    """базовий клас для вакцин"""
    pass


class NotVaccinatedError(VaccineError):
    """відвідувач немає ключа vaccine"""
    pass


class OutdatedVaccineError(VaccineError):
    """вакцина прострочена"""
    pass


class NotWearingMaskError(Exception):
    """відвідувач не носить маску"""
    pass
