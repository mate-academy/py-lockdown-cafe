class VaccineError(Exception):
    """Base class for vaccination-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Ошибка: вакцина отсутствует."""
    pass


class OutdatedVaccineError(VaccineError):
    """Error: The vaccine has expired."""
    pass


class NotWearingMaskError(Exception):
    """Error: Visitor without a mask."""
    pass
