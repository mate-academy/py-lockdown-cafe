class VaccineError(Exception):
    def __init__(
        self,
        message: str = "Visitors hav problems with their vaccine"
    ) -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message


class NotVaccinatedError(VaccineError):
    def __init__(
            self,
            message: str = "NotVaccinatedError, "
                           "some visitor/s do not have vaccination"
    ) -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message


class OutdatedVaccineError(VaccineError):
    def __init__(
            self,
            message: str = "OutdatedVaccineError, "
                           "some visitor/s have expired vaccination"
    ) -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message


class NotWearingMaskError(Exception):
    def __init__(
            self,
            message: str = "NotWearingMaskError, "
                           "some visitor/s do not wear a mask"
    ) -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message
