class VaccineError(Exception):
    def __init__(self) -> None:
        self.message = "VaccineError"

    def __str__(self) -> str:
        return self.message


class NotVaccinatedError(VaccineError):
    def __init__(self) -> None:
        self.message = "NotVaccinatedError"

    def __str__(self) -> str:
        return self.message


class OutdatedVaccineError(VaccineError):
    def __init__(self) -> None:
        self.message = "OutdatedVaccineError"

    def __str__(self) -> str:
        return self.message


class NotWearingMaskError(Exception):
    def __init__(self) -> None:
        self.message = "NotWearingMaskError"

    def __str__(self) -> str:
        return self.message
