class VaccineError(Exception):
    """Error for vaccine problems"""


class NotVaccinatedError(VaccineError):
    """Error for not vaccinated visitors"""

    def __str__(self) -> str:
        return "You have to be vaccinated!"


class OutdatedVaccineError(VaccineError):
    """Error for vaccine that is outdated"""

    def __str__(self) -> str:
        return "Your vaccine must not be outdated!"


class NotWearingMaskError(Exception):
    """Error for visitor who don't wear mask on"""

    def __str__(self) -> str:
        return f"You should buy mask!"
