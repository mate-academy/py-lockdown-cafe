class VaccineError(Exception):
    def __str__(self) -> str:
        return f"{self.__class__.__name__}"


class NotVaccinatedError(VaccineError):
    """Person is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """The vaccine term has expired"""


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return f"{self.__class__.__name__}"
