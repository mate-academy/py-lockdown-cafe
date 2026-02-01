class VaccineError(Exception):
    """No vaccine or have outdated one error"""


class NotVaccinatedError(VaccineError):
    """No vaccine error"""
    def __str__(self) -> str:
        return "You should be vaccinated to visit our cafe"


class OutdatedVaccineError(VaccineError):
    """Vaccination is outdated error"""
    def __str__(self) -> str:
        return ("Your vaccination is outdated, "
                "you should remake it to visit our cafe")


class NotWearingMaskError(Exception):
    """No mask error"""
    def __str__(self) -> str:
        return "You should wear mask to visit our cafe"
