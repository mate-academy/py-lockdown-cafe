class NotWearingMaskError(Exception):
    """
        Not Wearing Mask Error
    """


class VaccineError(Exception):
    def __init__(
        self,
        message: str = "All friends should be vaccinated"
    ) -> None:
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    """
        Not Vaccinated Error
    """


class OutdatedVaccineError(VaccineError):
    """
        Outdated Vaccine Error
    """
