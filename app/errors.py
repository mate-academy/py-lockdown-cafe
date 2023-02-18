class VaccineError(Exception):
    """The exception is raised
    when there is some problems with vaccination"""


class NotVaccinatedError(VaccineError):
    def __init__(
            self,
            message: str = "Vaccine is obligatory!"
    ) -> None:
        self.message = message
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(
            self,
            message: str = "Your vaccine has been expired."
    ) -> None:
        self.message = message
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(
            self,
            message: str = "The mask wearing is obligatory here."
    ) -> None:
        self.message = message
        super().__init__(message)
