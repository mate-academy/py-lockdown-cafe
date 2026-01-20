class VaccineError(Exception):
    """Base class for vaccine related errors."""
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, message: str = "Visitor is not vaccinated"):
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message: str = "Vaccine is outdated"):
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self, message: str = "Visitor is not wearing a mask"):
        super().__init__(message)
