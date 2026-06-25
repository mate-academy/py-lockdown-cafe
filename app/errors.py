class VaccineError(Exception):
    """Vaccine Error - parent class"""


class NotVaccinatedError(VaccineError):
    """Not Vaccinated Error - Vaccine Error child class"""
    def __init__(
            self,
            message: str = "You should vaccinate!"
    ) -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    """Outdated Vaccine Error - Vaccine Error child class"""
    def __init__(
            self,
            message: str = "Your vaccine is outdated. "
                           "You should vaccinate!"
    ) -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    """Not Wearing Mask Error - Vaccine Error child class"""
    def __init__(
            self,
            message: str = "You should wear a mask!"
    ) -> None:
        super().__init__(message)
