class VaccineError(Exception):
    """This exception is raised when one of the
    guests has a problem with vaccination"""


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "You must be vaccinated!"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Your vaccine has expired"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "You must wear a mask!"
